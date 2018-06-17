# coding=utf-8

import requests
import io
import os
import json


POST_URL = 'http://fraction.im/api/v1/microblog/'


class FractionChartError(Exception):
    pass


def push(token, plot, title, code_snippet, comment=None, data_set=None, path_to_csv=None):
    """
    Pushes a plot to the website via a POST request

    Args:
        token (str): Token for user authentication.
        plot (fig): Matplotlib figure object
        title (str): Title to display along with the chart
        code_snippet (str): Code snippet used to generate plot
        comment (str): A brief description or comment to post with chart
        data_set (JSON str): Keys are column names and Values are numpy arrays
        path_to_csv (str): Path to a CSV data file
    :rtype: The JSON output from the API or an error message
    """
    # validation
    if not token:
        raise Exception('You must provide a token for authentication.')

    if not plot:
        raise Exception('You must provide a Matplotlib figure object.')

    if not title:
        raise Exception('You must provide a title for your chart.')

    if not code_snippet:
        raise Exception('You must provide code_snippet.')

    if data_set:
        try:
            json_obj = json.loads(data_set)
        except Exception:
            raise ValueError('The data_set that you passed is not valid.\nIt should be valid JSON string.')

    # save to in-memory file
    buf = io.StringIO()
    try:
        plot.savefig(buf, format='svg')

        if path_to_csv and os.path.exists(path_to_csv):
            files = {'chart': buf.getvalue(), 'csv_file': open(path_to_csv, 'r')}
        else:
            files = {'chart': buf.getvalue()}
    except AttributeError:
        raise ValueError(
            """
            The plot you passed is not valid. It should be valid Matplotlib figure object, which can generate a chart.
            
            For example:
                import matplotlib.pyplot as plt
                plt.figure()
                plt.plot([1, 2])
                plt.title("test")                
                
            
            As you can see the example above, you can pass the 'plt' object to our param:'plot'.
            """
        )
    except Exception as e:
        raise Exception(e)

    finally:
        buf.close()

    try:

        headers = {
            'Authorization': "Token %s" % token,
            'Cache-Control': "no-cache"
        }

        data = {
            "name": title,
            "code_snippet": code_snippet,
            "comment": comment,
            "data_set": data_set
        }

        r = requests.post(POST_URL, files=files, data=data, headers=headers)

        if r.status_code >= 400:
            # in case of a 500 error,  the response might not be a json
            try:
                error_data = r.json()
            except ValueError:
                error_data = {'response': r}
            raise FractionChartError(error_data)

        if r.status_code == 204:
            return None

        return r.json()

    except Exception as e:
        raise Exception(e)

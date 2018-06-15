import requests
import io
import os
import json


POST_URL = 'http://fraction.im/api/v1/microblog/'


def push(token, plot, name, code_snippet, comment=None, data_set=None, path_to_csv=None):
    """
    Pushes a plot to the website via a POST request

    Args:
        token (str): Token for user authentication.
        plot (fig): Matplotlib figure object
        name (str): Name to display along with the chart
        code_snippet (str): Code snippet used to generate plot
        comment (str): A brief description or comment to post with chart
        data_set (JSON str): Keys are column names and Values are numpy arrays
        path_to_csv (str): Path to a CSV data file
    :rtype: requests.Response
    """
    # validation
    if code_snippet is None:
        raise ValueError('Parameter:"code_snippet" should not be empty.')

    if data_set:
        try:
            json_obj = json.loads(data_set)
        except Exception:
            raise ValueError('Parameter:"data_set" should be valid JSON string.')

    # save to in-memory file
    buf = io.StringIO()
    try:
        plot.savefig(buf, format='svg')

        if path_to_csv and os.path.exists(path_to_csv):
            files = {'chart': buf.getvalue(), 'csv_file': open(path_to_csv, 'r')}
        else:
            files = {'chart': buf.getvalue()}
    except AttributeError:
        raise ValueError('Parameter:"plot" should be figure object')

    except Exception as e:
        raise Exception(e)

    finally:
        buf.close()

    headers = {
        'Authorization': "Token %s" % token,
        'Cache-Control': "no-cache"
    }

    data = {
        "name": name,
        "code_snippet": code_snippet,
        "comment": comment,
        "data_set": data_set
    }

    return requests.post(POST_URL, files=files, data=data, headers=headers)

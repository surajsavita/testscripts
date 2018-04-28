from urllib2 import HTTPError
import json
import sys
import urllib2

'''

usage:
    cat list_of_repos | python ./github_stats.py
    
'''

def print_stats():
    lines = sys.stdin.readlines()
    # print(lines)
    if lines:
        print("Name,Clone URL,Latest Commit Date,Latest Author")

    for repo_name in lines:

        try:
            # name = "kubernetes/charts"
            name = str(repo_name).strip()
            url = 'https://api.github.com/repos/{}/commits'.format(name)
            # print(url, name, repo_name)
            response = urllib2.urlopen(url)
            data = json.load(response)
            row = [name, "git@github.com:{}.git".format(name), str(data[0]['commit']['author']['date']),
                   str(data[0]['commit']['author']['name'])]
            print(",".join(row))
        except HTTPError as e:
            print(repo_name, '### Bad Repo ###')


if __name__ == '__main__':

    print_stats()

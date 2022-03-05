from gh_helper import Bot
from time import sleep

# USERNAME = "sujeetgh"
USERNAME = "Amit-kharod"

def main():

    bot = Bot()
    repos = bot.fetch_repos(username=USERNAME)

    # TODO app will send welcome msg and current repos

    bot.send_msg(
f"""Hey Sujeet!
I will let you know as soon as Amit creates any new repo on github.
I will check for update in every 15 minutes.
Current repos are:
"""+str(repos)
    )

    repo_count = len(repos) if repos else 0
    while True:
        repos = bot.fetch_repos(username=USERNAME)

        if not repos: return
        if len(repos) > repo_count:
            repo_count = len(repos)
            bot.send_msg(
"""New repo was created in Amit's github account!
Current repos list:
""" + str(repos)
           )

        sleep(15*60) # 15 minutes

if __name__ == "__main__":
    main()





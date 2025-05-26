# Bait-Bot
Discord Bot that Roasts your friends/ rage baits them. Run it yourself! (Is a GPT wrapper)


**Setup**
You're going to need an Open AI API Key as well as a Discord API Key: See references for details:

For Open AI API Key. Give all permissions.
https://openai.com/api/ 

Discord API Key for Bot:
https://discord.com/developers/docs/reference

How to get Server and Channel ID:
https://docs.statbot.net/docs/faq/general/how-find-id/#:~:text=First%20make%20sure%20you%20have,or%20on%20a%20text%20editor.

Once you have all of that information, put it in the .env file.

Also, fill out the profiles.txt with any info that can be used to roast your teammates

**How to Run**
The easiest way to do this is to pull the docker image from my repository use the command 


```
docker pull nomangoesforyou/bait_bot:1.1
````



From there, you can just mount the .env and profiles.txt file using



```
docker run -v </path/to/your/.env && profiles.txt/on/host:/app bait_bot:1.1
```

**Build it yourself**

Feel free to build it yourself using the provided Dockerfile and python files. 



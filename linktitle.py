from __future__ import print_function

# url_finder = None

def setup(bot=None):
   pass
   # global url_finder
   # url_finder = re.compile(r'(?u)(%s?(?:http|https|ftp)(?:://\S+))' %
   #        (bot.config.url.exclusion_char), re.IGNORECASE)

try:
    import sopel.module
except ImportError:
    # Probably running from commandline
    pass
else:
   @rule('(?u).*(https?://\S+).*')
   def title_auto(bot, trigger):
      pass
      # if re.match(bot.config.core.prefix + 'title', trigger):
      #    return
      # # Avoid fetching known malicious links
      #  if 'safety_cache' in bot.memory and trigger in bot.memory['safety_cache']:
      #     if bot.memory['safety_cache'][trigger]['positives'] > 1:
      #        return
      #  urls = re.findall(url_finder, trigger)
      #  if len(urls) == 0:
      #     return
      #  results = process_urls(bot, trigger, urls)
      #  bot.memory['last_seen_url'][trigger.sender] = urls[-1]

      #  for title, domain in results[:4]:
      #     message = '[ %s ] - %s' % (title, domain)
      #      # Guard against responding to other instances of this bot.
      #      if message != trigger:
      #         bot.say(message)

if __name__ == '__main__':
   # import sys
   # if len(sys.argv) > 1:
   #     query = ' '.join(sys.argv[1:])
   # print('Looking up "{}"'.format(query))
   # results = process_urls(query)
   # if results:
   #     for result in results:
   #         print("Time for {} is {} ({})".format(*result))
   # else:
   #     print('Couldn\'t look up time for "{}"'.format(query))
   pass

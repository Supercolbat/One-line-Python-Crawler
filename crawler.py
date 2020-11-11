with type("Crawler", (), {
    # necessary for doing with ... as ...
    "__enter__": lambda s: s,
    "__exit__": lambda s, e, v, t: 1,

    # importing modules
    "requests": __import__("requests"),
    "bs4": __import__("bs4"),
    "urljoin": lambda s, b, u: __import__("urllib").parse.urljoin(str(b), str(u)),

    # settings variables
    "args": __import__("sys").argv,
    "__init__": lambda s: [
        None,
        setattr(s, "links", []),
        setattr(s, "unchecked", []),
        setattr(s, "file", None)
    ][0], # __init__ must always return None

    # main program
    "crawl": lambda crawler, url, fn, depth=5: [run for run in [
        # open the file and save to variable
        setattr(crawler, "file", open(fn, "w", encoding="utf-8")),
        setattr(crawler, "unchecked", [url]),
        (lambda: [

            # add new links to unchecked list
            [(lambda l:\
                [
                    # scrape all links from a page and loop through them
                    # check if the link has an href tag, hasn't already been found, and doesn't begin with '#'
                    # append the link to the "unchecked" variable
                    getattr(crawler, "unchecked").append(crawler.urljoin(str(url), link["href"]))
                    for link in crawler.bs4.BeautifulSoup(crawler.requests.get(l, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}).text, features="html.parser", parse_only=crawler.bs4.SoupStrainer("a"))
                    if link.has_attr("href") and not link["href"] in [gettattr(crawler, "unchecked"), getattr(crawler, "links")] and not link["href"][0] == "#"
                ] or \
                (lambda: getattr(crawler, "links").append(l) or getattr(crawler, "unchecked").pop(i))() # append l to the "links" variable and remove from unchecked
            )(l) for i, l in enumerate(crawler.unchecked)] # loop through unchecked links

            # repeat code above "depth" amount of times (WIP)
            for lvl in range(depth)
        ])(),
        # write links to file and close
        getattr(crawler, "file").write("\n".join([crawler.urljoin(str(url), l) for l in crawler.links])),
        getattr(crawler, "file").close()
    ]]
})() as crawler: crawler.crawl(
    crawler.args[crawler.args.index("-u") + 1], # get the value after -u (url)
    crawler.args[crawler.args.index("-f") + 1], # get the value after -f (file)
    int(crawler.args[crawler.args.index("-d") + 1]) if "-d" in crawler.args else 5  # get the value after -d (depth) or default to 5
)\
if not "-h" in __import__("sys").argv else\
print(f"usage: python {__import__('os').path.basename(__file__)} -u <url> -f <file>\n\nMade in 1 line of code by Joey Lent.\nIf nothing is outputted when the program ends, then either an error occured or no links were found on the website.\nIf the program hangs, then the site is preventing a request from being made.")
# show help message if "-h" flag is present

print(crawler.unchecked)
print(crawler.links)
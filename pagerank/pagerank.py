import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    #raise NotImplementedError
    #ST

    transition={}
    if len(corpus[page])>0:
        for key in corpus:
            transition[key]=(1-damping_factor)/len(corpus)    
        for element in corpus[page]:
            transition[element]+=(damping_factor/len(corpus[page]))
    else:
        for key in corpus:
            transition[key]=1/len(corpus)

    return transition
    
    
    #/ST


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    #raise NotImplementedError
    #ST

    pagesrank={}
    for key in corpus:
        pagesrank[key]=0
    page= random.choice(list(pagesrank))
    for i in range(n):
        transition=transition_model(corpus,page,damping_factor)
        pagelist=[]
        ranklist=[]
        for key in pagesrank:
            pagesrank[key]=transition[key]
            pagelist.append(key)
            ranklist.append(pagesrank[key]*10)
        page_l=random.choices(pagelist,weights=ranklist,k=1)
        page=page_l[0]

    return pagesrank
    
    
    #/ST


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    #ST

    b_pagesrank={}
    pagesrank={}
    for key in corpus:
        pagesrank[key]=1/(len(corpus))
        
        
    while(True):
        for key in pagesrank:
            b_pagesrank[key]=pagesrank[key]
        for key in pagesrank:
            pagesrank[key]=PR(corpus, damping_factor,b_pagesrank,key)
        if cond(pagesrank,b_pagesrank) is not True:
            return pagesrank
        
    
    
    
    #/ST
def PR(corpus, damping_factor, before,p):

    pr=(1-damping_factor)/len(corpus)

    summa=0
    for i in corpus:
        if p in corpus[i]:           
            summa+=(before[i]/len(corpus[i]))
        elif len(corpus[i])==0:
            summa+=(1/(len(corpus)))

    
    pr+=(damping_factor*summa)
    
    return pr

def cond (dict1,dict2):
    for key in dict1:
        if (abs(dict1[key]-dict2[key])>0.001):
            return True
    return False

if __name__ == "__main__":
    main()

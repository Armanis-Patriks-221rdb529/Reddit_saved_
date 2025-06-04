from re_praw import fethcdata
from hashtab import HashTable
from convert import download, folder_path



if __name__ == '__main__':

    fethcdata()

    try:
        with open('processed.txt', 'x') as f:
            print('izveidots processed.txt')
    except FileExistsError:
        print('processed.txt jau izveidots')
    
    ht = HashTable(1009)
    with open('saved_posts.txt', 'r') as f:
        saved_urls = [line.strip() for line in f if line.strip()]
        for url in saved_urls:
            ht.insert(url, None)

    ht_processed = HashTable(1009)
    with open('processed.txt', 'r') as f:
        processed_urls = [line.strip() for line in f if line.strip()]
        for url in processed_urls:
            ht_processed.insert(url, None)

    with open('processed.txt', 'a') as fout:
        count = 0
        #print('' in ht)
        for url in saved_urls:
            if url not in ht_processed:
                good = download(url, folder_path)
                ht_processed.insert(url, None)
                fout.write(url + '\n')
            else:
                count += 1

    print('Urls daudzums kuri tika izlaisti:', count)

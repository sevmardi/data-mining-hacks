import hashlib
import zlib
import nltk
from timeit import default_timer as timer

def hash_CRC32(s):
    return zlib.crc32(s) & 0xffffff

def hash_Adler32(s):
    return zlib.adler32(s) &  0xffffff

def hash_MD5(s):
    return int(hashlib.md5(s).hexdigest(), 16) & 0xffffff

def hash_SHA(s):
    return int(hashlib.sha1(s).hexdigest(), 16) & 0xffffff

hash_functions = [hash_CRC32, hash_Adler32, hash_MD5, hash_SHA]

def main():
	start_time = timer()
	 if len(sys.argv) < 1:
        raise ValueError("No arguments were provided\n"
                         % sys.argv[0])
    # words = nltk.corpus.gutenberg.words('austen-persuasion.txt')
    # words = [x.lower().encode('utf-8') for x in words]
    # print(len(words))
    # words[1:8]


if __name__ == '__main__':
    main()

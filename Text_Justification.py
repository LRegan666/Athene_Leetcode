class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        tmp, res = '', []
        num_tmp = 0
        for i in range(len(words)):
            if num_tmp < maxWidth:
                if not tmp:
                    tmp = words[i]
                    num_tmp += len(words[i])
                else:
                    tmp = tmp + ' ' + words[i]
                    num_tmp = num_tmp + 1 + len(words[i])
            elif num_tmp == maxWidth:
                res.append(tmp)
                tmp, num_tmp = words[i], len(words[i])
            else:
                tmp, num_tmp = self._text_adjust(tmp, num_tmp, maxWidth, words[i], res)
        if 0 < num_tmp < maxWidth:
            tmp = tmp + ' ' * (maxWidth - num_tmp)
            res.append(tmp)
            num_tmp = 0
        if num_tmp == maxWidth:
            res.append(tmp)
            num_tmp = 0
        if num_tmp > maxWidth:
            tmp, num_tmp = self._text_adjust(tmp, num_tmp, maxWidth, '', res)
            tmp = tmp + ' ' * (maxWidth - num_tmp)
            res.append(tmp)
        return res

    def _text_adjust(self, tmp, num_tmp, maxWidth, word, res):
        cur_words = tmp.split(' ')
        tmp = ''
        num_tmp = num_tmp - 1 - len(cur_words[-1])
        blanks = maxWidth - num_tmp
        num_blank = len(cur_words[:-1]) - 1
        avg = 0 if num_blank == 0 else int(round(float(blanks) / num_blank))
        blanks_var = blanks
        for i in range(len(cur_words)-1):
            if not tmp:
                tmp = cur_words[i]
            else:
                if avg == 0:
                    if blanks_var > 0:
                        L = 2
                        blanks_var -= 1
                    else:
                        L = 1
                else:
                    rd = blanks - (num_blank - 1) * avg
                    if rd >= 0:
                        if rd > avg:
                            L = rd + 1 if i == 1 else avg + 1
                        else:
                            L = rd + 1 if i == len(cur_words) - 2 else avg + 1
                    else:
                        if blanks_var > 0:
                            L = 2
                            blanks_var -= 1
                        else:
                            L = 1
                tmp = tmp + ' ' * L + cur_words[i]
        if num_blank == 0:
            tmp += ' ' * blanks
        res.append(tmp)
        if word:
            tmp = cur_words[-1] + ' ' + word
            num_tmp = len(cur_words[-1]) + 1 + len(word)
        else:
            tmp = cur_words[-1]
            num_tmp = len(cur_words[-1])
        return tmp, num_tmp


if __name__ == '__main__':
    words = ["When","I","was","just","a","little","girl","I","asked","my","mother","what","will","I","be","Will","I","be","pretty","Will","I","be","rich","Here's","what","she","said","to","me","Que","sera","sera","Whatever","will","be","will","be","The","future's","not","ours","to","see","Que","sera","sera","When","I","was","just","a","child","in","school","I","asked","my","teacher","what","should","I","try","Should","I","paint","pictures","Should","I","sing","songs","This","was","her","wise","reply","Que","sera","sera","Whatever","will","be","will","be","The","future's","not","ours","to","see","Que","sera","sera","When","I","grew","up","and","fell","in","love","I","asked","my","sweetheart","what","lies","ahead","Will","there","be","rainbows","day","after","day","Here's","what","my","sweetheart","said","Que","sera","sera","Whatever","will","be","will","be","The","future's","not","ours","to","see",
             "Que","sera","sera","What","will","be,","will","be","Que","sera","sera..."]
    maxWidth = 60
    res = Solution().fullJustify(words, maxWidth)
    print(res)


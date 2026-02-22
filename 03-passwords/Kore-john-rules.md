# KoreLogic John rules

KoreLogic used a variety of custom rules to generate the passwords. These same rules can be used to crack passwords in corporate environments. These rules were originally created because the default ruleset for John the Ripper fails to crack passwords with more complex patterns used in corporate environments.

Instruction for Use:

To use KoreLogic's rules in John the Ripper: download the rules.txt file - and perform the following command in the directory where your john.conf is located.

`cat rules.txt >> john.conf`

Example command lines are as follows:

* `./john -w:Lastnames.dic --format:nt --rules:KoreLogicRulesAdd2010Everywhere pwdump.txt`
* `./john -w:3EVERYTHING.doc --format:ssha --rules:KoreLogicRulesMonthsFullPreface fgdump.txt`
* `./john -w:Seasons.dic --format:md5 --rules:KoreLogicRulesPrependJustSpecials /etc/shadow`

Other Ideas:

```bash
for ruleset in `grep KoreLogicRules john.conf | cut -d: -f 2 | cut -d\] -f 1`; do
   echo ./john --rules:${ruleset} -w:sports_teams.dic --format:nt pwdump.txt
done
```

KoreLogic also provides two CHR files (used by John the Ripper) that allow for smarter brute forcing based on "Rock You" passwords. These CHR files are located at the following link

1) For LANMAN hashes: `./john --format:lm -i:RockYou-LanMan pwdump.txt`
2) For NTLM hashes (or others) `./john --format:nt -i:RockYou pwdump.txt`

## Notes for HashCat / PasswordPro Users:

Some of these rules can be converted to other formats in order to work with other password cracking tools. All rules that use A0 and AZ will specifically not easily convert to other formats. We strongly encourage you to convert these rules to other formats (PasswordPro / HashCat / etc) and share them with the password cracking community.

---

### KoreLogicRulesAppendNumbers_and_Specials_Simple:

This rule is a "catch all" for the most common patterns for appending numbers and/or specials to the end of a word. Use this rule _first_ before attempting other rules that use special characters

### KoreLogicRulesPrependSeason:

This rule prepends any word in the wordlist with a season (Fall FALL Winter WINTER etc). Use this rule with wordlists such as 2letters.dic or 2EVERYTHING.dic

### KoreLogicRulesAppendSeason:

This rule appends any word in the wordlist with a season (Fall FALL Winter WINTER etc). Use this rule with wordlists such as 2letters.dic or 2EVERYTHING.dic

### KoreLogicRulesPrependHello:

This rule prepends any word in the wordlist with the word 'Hello' (Hello hEllo heLLo hellO etc). Use this rule with wordlists such as 2letters.dic or 2EVERYTHING.dic

### KoreLogicRulesPrependYears:

This rule prepends any word in the wordlist with a year (from 1949 to 2019). These are common birth years of users, or their family members.

### KoreLogicRulesAppendYears:

This rule appends any word in the wordlist with a year (from 1949 to 2019). These are common birth years of users, or their family members.

### KoreLogicRulesAppendCurrentYearSpecial:

This rule appends the current year followed by a special character (2010! 2010# 2010$ 2010~ 2010~).

### KoreLogicRulesAppend4Num:

This rule appends 4 numbers to each word in the wordlist (0000 0001 0002 .... 9998 9999).

### KoreLogicRulesAppend5Num:

This rule appends 5 numbers to each word in the wordlist (00000 00001 00002 .... 99998 99999).

### KoreLogicRulesAppend6Num:

This rule appends 6 numbers to each word in the wordlist (000000 000001 000002 .... 999998 999999).

### KoreLogicRulesAppendSpecial3num:

This rule appends a special character - followed by 3 numbers.

### KoreLogicRulesAppendSpecial4num:

This rule appends a special character - followed by 4 numbers.

### KoreLogicRulesPrependCAPCAPAppendSpecial:

This rule prepends 2 capital letters - and appends a special character (AAword! ZZword?).

### KoreLogicRulesPrependNumNumAppendSpecial:

This rule prepends 2 numbers - and appends 1 special character.

### KoreLogicRulesPrependNumNum:

This rule prepends 2 numbers.

### KoreLogicRulesPrependNumNumNum:

This rule prepends 3 numbers.

### KoreLogicRulesPrependNumNumNumNum:

This rule prepends 4 numbers.

### KoreLogicRulesPrependNumNumSpecial:

This rule prepends 2 numbers then a special character (00!word 99# word .. etc).

### KoreLogicRulesPrepend2NumbersAppend2Numbers:

This rule prepends 2 numbers and then appends 2 numbers.

### KoreLogicRulesPrependSpecialSpecial:

This rule prepends 2 special characters

### KoreLogicRulesAppendSpecialNumberNumber:

This rule appends a special characters - and then 2 numbers.

### KoreLogicRulesAppendSpecialNumberNumberNumber:

This rule appends a special characters - and then 3 numbers.

### KoreLogicRulesPrependSpecialSpecialAppendNumber:

This rule prepends 2 special characters - and appends 1 number.

### KoreLogicRulesPrependSpecialSpecialAppendNumbersNumber:

This rule prepends 2 special characters - and appends 2 numbers.

### KoreLogicRulesPrependSpecialSpecialAppendNumbersNumberNumber:

This rule prepends 2 special characters - and appends 3 numbers.

### KoreLogicRulesAppend2Letters:

This rule appends 2 letters to the end of a word.

### KoreLogicRulesPrepend4NumAppendSpecial:

This rule prepends 4 Numbers - and then appends a special character to a word (1234word!).

### KoreLogicRulesAppend4NumSpecial:

This rule appends 4 Numbers - and then appends a special character to a word (word1234!).

### KoreLogicRulesAppend3NumSpecial:

This rule appends 3 Numbers - and then appends a special character to a word (word123!).

### KoreLogicRulesAppend2NumSpecial:

This rule appends 2 Numbers - and then appends a special character to a word (word12!).

### KoreLogicRulesAddJustNumbersLimit8:

This rule appends numbers to a password - but limits the length of the password to 8 chars. Useful for DES hashes, and also doesn't waste work adding 4 numbers to a word that is already 6 chars long.

### KoreLogicRulesDevProdTestUAT:

This rule either prepends or appends the strings UAT or DEV or PROD to a word. This is to take advantage of administrators laziness in labeling what environment the password originates from.

### KoreLogicRulesPrependAndAppendSpecial:

This rule both prepends and appends a special character to a word ( !word! $word? *word$ ).

### KoreLogicRulesAppendJustNumbers:

This rule appends just numbers to a word. Append 1 number (with and without capitalizing the Word). Append 2 numbers. Prepend 1 number. Prepend 2 numbers. Append 3 numbers, and prepend 3 numbers. This is a "catch all" for any password that begins and ends with a number.

### KoreLogicRulesAppendJustSpecials:

This rule appends just special characters to the end of each word. Examples: ( word$ Word$ word$! Word!$ ).

### KoreLogicRulesMonthsFullPreface:

This rule prepends entire months to the beginning of a word. Good to use with 2EVERYTHING.dic - not for use for large word-based dictionaries. Examples: ( December!! March123! AprilUAT October?? ).

### KoreLogicRulesAddShortMonthsEverywhere:

This rule puts abbreviated months of the year "inside" a word. Examples: ( JANword wJANord woJANrd worJANd wordJAN ). Use with 4EVERYTHING.dic for good 7 character results.

### KoreLogicRulesPrepend4LetterMonths:

This rule prepends abbreviated months (4 chars each) to the beginning of each word ( Febrword Januword Marcword Deceword ).

### KoreLogicRulesAdd2010Everywhere:

This rule places the string '2010' is all possible places inside of a word. Example: 2010word w2010ord wo2010rd wor2010d word2010. Useful with 4EVERYTHING.dic.

### KoreLogicRulesPrependDaysWeek:

This rule prepends the days of the week to the beginning of a word.

### KoreLogicRulesAdd1234_Everywhere:

This rule places the string '1234' is all possible places inside of a word. Example: 1234word w1234ord wo1234rd wor1234d word1234. Useful with 4EVERYTHING.dic.

### KoreLogicRulesAppendMonthDay:

This rule appends a month and day to the end of a word. Examples: wordMay1 wordMay30 wordFeb12 wordfeb1 wordDec30

### KoreLogicRulesAppendMonthCurrentYear:

This rule appends a month and the current year to the end of a word. Examples: wordJan2010 wordMar2010 worddec2010

### KoreLogicRulesReplaceNumbers2Special:

This rule takes a list of words, and replaces all numbers to their 'shift' equivalent. Example: word1234 becomes: word!@#$. This is extremely useful after a large amount of passwords have been cracked and you have a list of previously cracked passwords, or if you have the password history for a particular user.

### KoreLogicRulesReplaceNumbers:

This rule takes a list of words, and replaces all numbers with other numbers. For example, word1 will become word0 word2 word3 word4 .... word9

### KoreLogicRulesReplaceLettersCaps:

This rule is a quick and dirty way to capitalize certain letters in the word. This is a very simple variation on what --rules:nt does in John the Ripper. --rules:nt generates a complete list of capitalization variations, where as KoreLogicRulesReplaceLettersCaps is _not_ complete, but does some quick variations. Examples: word becomes Word wOrd woRd worD ( but _not_ WOrd WoRd woRD ... etc).

### KoreLogicRulesAddDotCom:

This rule simply adds .com .net and .org to the end of a word. Example: word.com Word.com word.org Word.org word.net Word.net

### KoreLogicRulesAppendCap-Num_or_Special-Twice:

This rule appends a capital letter - followed by 2 numbers and/or special characters. Examples: WordA00 wordZ12 Word!0 Word5% Word?? word ^!

### KoreLogicRulesAppendSpecialLowerLower:

This rule appends a special character - followed by 2 lower case letters.

### KoreLogicRulesAppendJustSpecials3Times:

This rule appends special characters - 3 times. Examples: Word!!! word$!. Word:'? word=-)

### KoreLogicRulesPrependJustSpecials:

This rule appends special characters - 1 and 2 times. Examples: Word! word$ Word:' word-)

### KoreLogicRulesAppend1_AddSpecialEverywhere:

This rule appends the number '1' to the end of a word, and also places a special character in every other position in the word. Examples: !word1 w!ord1 wo$rd1 wor&d1 word:1

### KoreLogicRulesPrependNumNum_AppendNumSpecial:

This rule prepends 2 numbers - and appends a number then a special character to the end of a word. Examples: 00word0! 12Word9? 99word2.

### KoreLogicRulesAppendNum_AddSpecialEverywhere:

This rule appends 1 numbers to the end of a word - and also places a special character in all other positions. Examples: !word1 w?ord9 wo*rd3 wor&d8

### KoreLogicRulesAppendNumNum_AddSpecialEverywhere:

This rule appends 2 numbers to the end of a word - and also places a special character in all other positions. Examples: !word15 w?ord95 wo*rd35 wor&d85

### KoreLogicRulesAppendNumNumNum_AddSpecialEverywhere:

This rule appends 3 numbers to the end of a word - and also places a special character in all other positions. Examples: !word135 w?ord935 wo*rd335 wor&d835

### KoreLogicRulesAppendYears_AddSpecialEverywhere:

This rule appends common years the end of word - but also places a special character is all other positions: Examples: !word1995 w^ord2001 Wo%rd1974 Wor+d2010 word$2010

### KoreLogicRulesL33t:

This rule is an expanded version of the default John the Ripper "l33t" rules. This set of "l33t speak" rules is more verbose, and generates more possibilities.

### KoreLogicRulesReplaceSpecial2Special:

This rule will replace any special character in the word provided with all the other special characters. Extremely useful for large networks with commonly shared passwords. Examples: word! word@ word^ word(

### KoreLogicRulesReplaceLetters:

This rule will replace any letter in the word provided with all the other letters. Extremely useful for large networks with commonly shared passwords. Examples: word wore wort tord zord ward wold


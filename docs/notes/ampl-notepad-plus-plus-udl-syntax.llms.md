# AMPL Notepad++ UDL Syntax

Author

Gang He

Published

May 1, 2014

I use AMPL for my modeling stuff, and I like to use text editor to deal with coding. Notepad++ can be a good alternative to BBEdit but AMPL is not included in the UDL list yet. So you have to make your own, as I did. To save your time, you may copy the following text to your Notepad++ and save as ampl.xml file, or download from [here](../files/tools/ampl.xml), then import from “Language -\> Define your language -\> Import”.

Well, this is not a complete list, but fair enough, let me know if you have one. Enjoy!

``` xml
<NotepadPlus>

    <UserLang name="ampl" ext="" udlVersion="2.1">

        <Settings>

            <Global caseIgnored="yes" allowFoldOfComments="no" foldCompact="no" forcePureLC="0" decimalSeparator="0" />

            <Prefix Keywords1="no" Keywords2="no" Keywords3="no" Keywords4="no" Keywords5="no" Keywords6="no" Keywords7="no" Keywords8="no" />

        </Settings>

        <KeywordLists>

            <Keywords name="Comments">00# 01 02 03/* 04*/</Keywords>

            <Keywords name="Numbers, prefix1"></Keywords>

            <Keywords name="Numbers, prefix2"></Keywords>

            <Keywords name="Numbers, extras1"></Keywords>

            <Keywords name="Numbers, extras2"></Keywords>

            <Keywords name="Numbers, suffix1"></Keywords>

            <Keywords name="Numbers, suffix2"></Keywords>

            <Keywords name="Numbers, range"></Keywords>

            <Keywords name="Operators1"></Keywords>

            <Keywords name="Operators2"></Keywords>

            <Keywords name="Folders in code1, open"></Keywords>

            <Keywords name="Folders in code1, middle"></Keywords>

            <Keywords name="Folders in code1, close"></Keywords>

            <Keywords name="Folders in code2, open"></Keywords>

            <Keywords name="Folders in code2, middle"></Keywords>

            <Keywords name="Folders in code2, close"></Keywords>

            <Keywords name="Folders in comment, open"></Keywords>

            <Keywords name="Folders in comment, middle"></Keywords>

            <Keywords name="Folders in comment, close"></Keywords>

            <Keywords name="Keywords1">set&#x000D;&#x000A;reset&#x000D;&#x000A;param&#x000D;&#x000A;

node&#x000D;&#x000A;arc&#x000D;&#x000A;check&#x000D;&#x000A;union&#x000D;&#x000A;

setof&#x000D;&#x000A;default&#x000D;&#x000A;var&#x000D;&#x000A;all&#x000D;&#x000A;

out&#x000D;&#x000A;local&#x000D;&#x000A;initial&#x000D;&#x000A;complements&#x000D;&#x000A;

contains&#x000D;&#x000A;dimen&#x000D;&#x000A;div&#x000D;&#x000A;environ&#x000D;&#x000A;

logical&#x000D;&#x000A;option&#x000D;&#x000A;shell_exitcode&#x000D;&#x000A;

solve_exitcode&#x000D;&#x000A;solve_message&#x000D;&#x000A;solve_result&#x000D;&#x000A;

solve_result_num&#x000D;&#x000A;suffix&#x000D;&#x000A;table&#x000D;&#x000A;

until&#x000D;&#x000A;while&#x000D;&#x000A;within&#x000D;&#x000A;maximize&#x000D;&#x000A;

minimize&#x000D;&#x000A;display&#x000D;&#x000A;solve&#x000D;&#x000A;subject to&#x000D;&#x000A;binary&#x000D;&#x000A;symbolic&#x000D;&#x000A;print&#x000D;&#x000A;

printf&#x000D;&#x000A;</Keywords>

            <Keywords name="Keywords2">if&#x000D;&#x000A;then&#x000D;&#x000A;else&#x000D;&#x000A;

exists &#x000D;&#x000A;forall&#x000D;&#x000A;not&#x000D;&#x000A;in&#x000D;&#x000A;

notin&#x000D;&#x000A;inter&#x000D;&#x000A;cross&#x000D;&#x000A;and&#x000D;&#x000A;

by&#x000D;&#x000A;or&#x000D;&#x000A;prod&#x000D;&#x000A;less&#x000D;&#x000A;

for&#x000D;&#x000A;break&#x000D;&#x000A;continue</Keywords>

            <Keywords name="Keywords3">sum&#x000D;&#x000A;abs&#x000D;&#x000A;acos&#x000D;&#x000A;

acosh&#x000D;&#x000A;asin&#x000D;&#x000A;asinh&#x000D;&#x000A;atan&#x000D;&#x000A;

atan2&#x000D;&#x000A;atanh&#x000D;&#x000A;cos&#x000D;&#x000A;cosh&#x000D;&#x000A;

exp&#x000D;&#x000A;log&#x000D;&#x000A;log10&#x000D;&#x000A;max&#x000D;&#x000A;

min&#x000D;&#x000A;sin&#x000D;&#x000A;sinh&#x000D;&#x000A;sqrt&#x000D;&#x000A;

tan&#x000D;&#x000A;tanh&#x000D;&#x000A;Beta&#x000D;&#x000A;Cauchy&#x000D;&#x000A;

Exponential&#x000D;&#x000A;Gamma&#x000D;&#x000A;Irand224&#x000D;&#x000A;

Normal&#x000D;&#x000A;Nomal01&#x000D;&#x000A;Poisson&#x000D;&#x000A;

Uniform&#x000D;&#x000A;Uniform01&#x000D;&#x000A;num&#x000D;&#x000A;num0&#x000D;&#x000A;

ichar&#x000D;&#x000A;char&#x000D;&#x000A;length&#x000D;&#x000A;substr&#x000D;&#x000A;

sprintf&#x000D;&#x000A;match&#x000D;&#x000A;sub&#x000D;&#x000A;gsub&#x000D;&#x000A;

floor&#x000D;&#x000A;&#x000D;&#x000A;</Keywords>

            <Keywords name="Keywords4">card&#x000D;&#x000A;arity&#x000D;&#x000A;next&#x000D;&#x000A;

nextw&#x000D;&#x000A;prev&#x000D;&#x000A;prevw&#x000D;&#x000A;first&#x000D;&#x000A;

last&#x000D;&#x000A;member&#x000D;&#x000A;ord&#x000D;&#x000A;indexarity&#x000D;&#x000A;

interval&#x000D;&#x000A;integer&#x000D;&#x000A;ordered&#x000D;&#x000A;circular</Keywords>

            <Keywords name="Keywords5"></Keywords>

            <Keywords name="Keywords6"></Keywords>

            <Keywords name="Keywords7"></Keywords>

            <Keywords name="Keywords8"></Keywords>

            <Keywords name="Delimiters">00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23</Keywords>

        </KeywordLists>

        <Styles>

            <WordsStyle name="DEFAULT" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="COMMENTS" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="LINE COMMENTS" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="NUMBERS" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="KEYWORDS1" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" nesting="0" />

            <WordsStyle name="KEYWORDS2" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" nesting="0" />

            <WordsStyle name="KEYWORDS3" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="1" nesting="0" />

            <WordsStyle name="KEYWORDS4" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" nesting="0" />

            <WordsStyle name="KEYWORDS5" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="KEYWORDS6" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="KEYWORDS7" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="KEYWORDS8" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="OPERATORS" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" nesting="0" />

            <WordsStyle name="FOLDER IN CODE1" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="FOLDER IN CODE2" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="FOLDER IN COMMENT" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="DELIMITERS1" fgColor="0000A0" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="DELIMITERS2" fgColor="0000A0" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="DELIMITERS3" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="DELIMITERS4" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="DELIMITERS5" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="DELIMITERS6" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="DELIMITERS7" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

            <WordsStyle name="DELIMITERS8" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />

        </Styles>

    </UserLang>

</NotepadPlus>
```

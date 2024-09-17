<div style = "font-size: 18px; font-family: times">
    <div>
        <h1 style = "font-size: 40px"> 
            884. Uncommon Words from Two Sentences 
        </h1>
    </div>
    <div style = "margin: 20px">
        <div>
            <b> Type: </b>
            <span style = "color: green"> Easy </span>
        </div>
        <div>
            <b> Topics: </b>
            <span> Hash Table, String, Counting </span>
        </div>
        <div>
            <b> Companies: </b>
            <span> J.P. Morgan </span>
        </div>
    </div><hr>
    <div>
        <p>
            A <b>sentence</b> is a string of single-space separated words where each word consists only of lowercase letters.
        </p>
        <p>
            A word is <b>uncommon</b> if it appears exactly once in one of the sentences, and <b>does not appear</b> in the other sentence.
        </p>
        <p>
            Given two <b>sentences</b> <code style = "font-family: times">s1</code> and <code style = "font-family: times">s2</code>, return a <i>list of all the <b>uncommon words</b></i>. You may return the answer in <b>any order</b>.
        </p>
    </div><hr>
    <div>
        <div>
            <b> Example 1: </b>
            <div style = "margin: 20px">
                <b>Input:</b> s1 = "this apple is sweet", s2 = "this apple is sour"<br>
                <b>Output:</b> ["sweet","sour"]<br>
                <b>Explanation:</b><br>
                The word "sweet" appears only in s1, while the word "sour" appears only in s2.
            </div>
        </div>
        <div>
            <b> Example 1: </b>
            <div style = "margin: 20px">
                <b>Input:</b> s1 = "apple apple", s2 = "banana"<br>
                <b>Output:</b> ["banana"]<br>
            </div>
        </div>
    </div><hr>
    <div>
        <b> Constraint: </b>
        <ul>
            <li>
                <code style = "font-family: times">1 <= s1.length, s2.length <= 200</code>
            </li>
            <li>
                <code style = "font-family: times">s1</code> and <code style = "font-family: times">s2</code> consist of lowercase English letters and spaces.
            </li>
            <li>
                <code style = "font-family: times">s1</code> and <code style = "font-family: times">s2</code> do not have leading or trailing spaces.
            </li>
            <li>
                All the words in <code style = "font-family: times">s1</code> and <code style = "font-family: times">s2</code> are separated by a single space.
            </li>
        </ul>
    </div><hr>
</div>
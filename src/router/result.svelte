<script>
    import {question_ans} from './../global.js'
    import json from './../lib/distrolist.json'
    
    let question_ans_sub
    question_ans.subscribe(value => {
        question_ans_sub = value
    })
    
</script>
<h1>the result</h1>

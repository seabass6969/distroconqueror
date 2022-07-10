<script>
    import {question_ans} from './../global.js'
    import json from './../lib/distrolist.json'
    import link from 'svelte-spa-router'
    let question_ans_sub
    question_ans.subscribe(value => {
        question_ans_sub = value
    })
    const distrolist = json["distrolist"]
    console.log(question_ans_sub)
    console.log(distrolist.filter(x => x.based === "arch").filter(x=>x.rpi_support === true))
    
</script>
<h1>the result</h1>
{#if question_ans_sub == undefined}
<h1>Error please actually fill the form</h1>
<a href="/" use:link>go back</a>
{/if}


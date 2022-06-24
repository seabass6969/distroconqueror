<script>
    import Iconlink from './../component/iconlink.svelte'
    import {page, question_ans} from './../global.js'
    import {question_USAGE} from './../lib/question_list'
const page_list = ["first","usage","interfaceType"]
    let on_page
    page.subscribe(value => {
        on_page = value
    })
    let question_ans_sub
    question_ans.subscribe(value => {
        question_ans_sub = value
    })
function next(){
    page.set(page_list[page_list.indexOf(on_page)+1])
}
function previous(){
    page.set(page_list[page_list.indexOf(on_page)-1])
}
    let question = {usage:""}
    $:{
        question_ans.set(question)
        console.log(question_ans_sub)
    }

</script>

<main>
<div class="sidebar">
<Iconlink linkto="first" icon="home"/>
<Iconlink linkto="interfaceType" icon="monitor"/>
</div>
<div class="bodytext">
{#if on_page == "first"}
<h1>welcome to distro conqueror, where you choose the linux distro that best suit to you and the most human friendly way as possible.</h1>
<h2>Your would need to answer few question, each question is about your prefrence when using computer and usage</h2>
<h2>We don't collect data from you.</h2>
<h2>click next to start the test!!!</h2>
{:else if on_page == "usage"}
<h2>Whats your usage on your computer usually?</h2>
{#each question_USAGE.ans as usage}
<label>
<input type="radio" bind:group={question.usage} value={usage}>{usage}
</label>
<br>

{/each}
{:else if on_page == "interfaceType"}
<h2>interface type</h2>
{:else if on_page == "last"}
<h2>Results:</h2>
{/if}

{#if on_page !== "first"}
<button on:click={previous}>Previous</button>
{/if}
{#if on_page !== "last"}
<button on:click={next}>Next</button>
{/if}
</div>
</main>

<style>
.sidebar{
height: 100%;
width: 100px;
position: fixed;
left: 0;
top: 0;
padding-top: 20px;
background-color: lightblue;
}


.bodytext{
margin-left: 100px;
}

</style>

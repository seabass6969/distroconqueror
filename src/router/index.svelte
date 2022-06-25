<link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
<script>
    import Iconlink from './../component/iconlink.svelte'
    import {page, question_ans} from './../global.js'
    import {question_USAGE} from './../lib/question_list'
const page_list = ["first","usage","interfaceType","computersavyrate","machineage","last"]
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
    let nextdisable = false
    let question = {usage:"",interfaceType:"",computersavyrate: "",machineage:""}
    $:{
        question_ans.set(question)
        console.log(question_ans_sub)
        if(question_ans_sub[on_page] == '' &&on_page !== "first"){nextdisable = true}
        else{
            nextdisable = false
        }
    }

</script>

<main>
<div class="sidebar">
<Iconlink linkto="first" icon="home"/>
<Iconlink linkto="usage" icon="data_usage"/>
<Iconlink linkto="interfaceType" icon="monitor"/>
<Iconlink linkto="computersavyrate" icon="gpp_good"/>
<Iconlink linkto="machineage" icon="elderly_woman"/>
</div>
<div class="bodytext">
{#if on_page == "first"}
<h1>welcome to distro conqueror, where you choose the linux distro that best suit to you and the most human friendly way as possible.</h1>
<h2>Your would need to answer few question, each question is about your prefrence when using computer and usage</h2>
<h2>We don't collect data from you.</h2>
<h2>click next to start the test!!!</h2>
{:else if on_page == "usage"}
<h2>Whats your usage on your computer usually? It make sure that you have the most user friendly and provide the appropate tools on the platform you would use.<div class="red">*(require)</div></h2>
{#each question_USAGE.ans as usage}
<label>
<input type="radio" bind:group={question.usage} value={usage}>{usage}
</label>
<br>

{/each}
{:else if on_page == "interfaceType"}
<h2>interface type. This determint what kind of user interface you want to try out or comfortable with. In Linux you have huge choice over everything including you user interface.</h2>
<div class="hoverbox">
<label>
<input type="radio" bind:group={question.interfaceType} value="windows"><h3 class="imagetext">I prefer windows™ like window manger<a class="material-icons" href="https://kde.org/plasma-desktop/">link</a></h3><img src="https://kde.org/announcements/plasma/5/5.25.0/fullscreen_with_apps.png" alt="kde plasma" class="scaleimage">
</label>
</div>
    <br>
<div class="hoverbox">
<label>
<input type="radio" bind:group={question.interfaceType} value="macos"><h3 class="imagetext">I prefer MacOS™ like window manger<a class="material-icons" href="https://elementary.io/">link</a></h3><img src="https://elementary.io/images/screenshots/desktop.jpg" alt="elementary OS" class="scaleimage">
</label>
</div>
    <br>
<div class="hoverbox">
<label>
<input type="radio" bind:group={question.interfaceType} value="tiling"><h3 class="imagetext">I prefer tiling window manger<a class="material-icons" href="https://www.reddit.com/r/unixporn/comments/vjdqkx/dwm_few_improvements_on_my_rice_removed_gaps_for/">link</a></h3><img src="https://preview.redd.it/0ipd1c0kbh791.png?width=640&crop=smart&auto=webp&s=f73b9521bcd6f4ceb1d7862d21471b646f2da9fa" alt="by u/weebcyberpunk" class="scaleimage">
</label>
</div>
    <br>
<div class="hoverbox">
<label>
<input type="radio" bind:group={question.interfaceType} value="none"><h3 class="imagetext">I have no idea</h3>
</label>
</div>
{:else if on_page == "computersavyrate"}
<h2>How good do you rate yourself when using computer?</h2>
<label>
<input type="radio" bind:group={question.computersavyrate} value="outstanding">I am able to use Linux proffessionally
</label>
<br>
<label>
<input type="radio" bind:group={question.computersavyrate} value="good">I could do programming and able to compile the program myself 
</label>
<br>
<label>
<input type="radio" bind:group={question.computersavyrate} value="neargood">I am able to solve my grandma computer problem
</label>
<br>
<label>
<input type="radio" bind:group={question.computersavyrate} value="nearbad">I am able browse the internet myself, but I need to ask people about some computer question
</label>
<br>
<label>
<input type="radio" bind:group={question.computersavyrate} value="bad">I need to always ask people about some computer question
</label>
{:else if on_page == "machineage"}
<h2>Linux can use on any hardware (including your smart toaster and smart fridge)What good is your computer preform</h2>
{:else if on_page == "last"}
<h2>Results:</h2>
{/if}

<br>

{#if on_page !== "first"}
<button on:click={previous}>Previous</button>
{/if}
{#if on_page !== "last"}
<button on:click={next} disabled={nextdisable}>Next</button>
{#if on_page !== "first"}
<button on:click={next}>skip</button>
{/if}
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

.red{
    color:red;
}
.scaleimage{
    width:450px
}
.hoverbox{
    border-style:solid; 
}
</style>

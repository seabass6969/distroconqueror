<script>
    import {page} from './../global.js'
    export let linkto = "first"
    export let icon = "home"
    let on_page
    page.subscribe(value => {
        on_page = value
    })
    function clicked(){
        page.set(linkto)
    }
</script>
<style>
.btnlogo{
    border:none;
    outline:none;
    appearance: none;
    background-color:transparent;
    cursor:pointer;
    
}
.material-icons {
font-size:50px;
user-select: none;
}
.itembar{
    align-items: center;
    display: flex;
    justify-content: center;
    width:100px;
    height:100px;
}
.on{
    color:tomato;
    text-shadow: 0 0 5px #FF0000;
}

</style>
<link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
<div class="itembar">
<button class="btnlogo" on:click={clicked}>
{#if on_page == linkto}
<span class="material-icons paddingbar on">{icon}</span>
{:else}
<span class="material-icons paddingbar">{icon}</span>
{/if}
</button>
</div>

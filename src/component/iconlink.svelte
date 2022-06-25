<script>
    import {page} from './../global.js'
    export let linkto = "first"
    export let icon = "home"
    export let on_color = "tomato"
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
    
    text-shadow: 0 0 5px #FF0000;
}
@media (max-width: 600px){
    .material-icons {
        font-size:30px;
    }
    .itembar{
        width:60px;
        height:60px;
    }
}
</style>
<link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
<div class="itembar">
<button class="btnlogo" on:click={clicked}>
{#if on_page == linkto}
<span class="material-icons paddingbar on" style="color:{on_color};">{icon}</span>
{:else}
<span class="material-icons paddingbar">{icon}</span>
{/if}
</button>
</div>

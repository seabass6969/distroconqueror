<script>
    import Router from 'svelte-spa-router'
    import Index from './router/index.svelte'
    import Result from './router/result.svelte'
    const routes = {
        '/': Index,
        '/result': Result
    }
</script>
<Router {routes} />


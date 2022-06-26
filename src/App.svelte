<script>
	import { Router, Link, Route } from "svelte-navigator";
    import Index from './router/index.svelte'
    import Result from './router/result.svelte'
</script>
<Router>
<Route path="/"><Index /></Route>
<Route path="/result"><Result /></Route>
</Router>

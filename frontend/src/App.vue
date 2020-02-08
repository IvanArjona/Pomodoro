<template>
  <div>
    <StartForm/>
    <Timer/>
  </div>
</template>

<script>
import StartForm from './components/StartForm.vue'
import Timer from './components/Timer.vue'

export default {
  name: 'App',
  data() {
    return {
      task: null,
      duration: null,
      shortBreakDuration: null,
      longBreakDuration: null,
      longBreakAfter: null
    }
  },
  components: {
    StartForm,
    Timer
  }
}
</script>

<style>

</style>

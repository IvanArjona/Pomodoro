<template>
  <footer class="footer d-flex justify-content-between">
    <History/>
    <span class="pointer" @click="startNew()">Start a new pomodoro</span>
  </footer>
</template>

<script>
import History from './History';

export default {
  methods: {
    startNew() {
      this.$emit('reset');
    },
    showHistory() {

    }
  },
  components: {
    History
  }
}
</script>

<style>
.footer {
  position: absolute;
  bottom: 0;
  padding: 1rem;
  width: 100%;
}
</style>
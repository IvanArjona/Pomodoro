<template>
  <footer class="footer d-flex justify-content-between">
    <span @click="showHistory()">History</span>
    <span @click="startNew()">Start a new pomodoro</span>
  </footer>
</template>

<script>
export default {
  methods: {
    startNew() {
      this.$emit('reset');
    },
    showHistory() {

    }
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
.footer > span {
  cursor: pointer;
}
</style>
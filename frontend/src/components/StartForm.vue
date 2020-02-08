<template>
  <form @submit.prevent="submit()">
    <h1>Start a pomodoro</h1>
    <div class="form-group">
      <label for="task">Task</label>
      <input type="text" id="task" class="form-control" v-model="task" required>
    </div>
    <div class="form-group">
      <label for="duration">Pomodoro duration</label>
      <input type="number" id="duration" class="form-control" min="1" v-model="duration">
      <small class="form-text muted">In minutes</small>
    </div>
    <div class="form-group">
      <label for="short-break">Short break duration</label>
      <input type="number" id="short-break" class="form-control" min="1" v-model="shortBreakDuration">
      <small class="form-text muted">In minutes</small>
    </div>
    <div class="form-group">
      <label for="long-break">Long break duration</label>
      <input type="number" id="long-break" class="form-control" min="1" v-model="longBreakDuration">
      <small class="form-text muted">In minutes</small>
    </div>
    <div class="form-group">
      <label for="long-break">Long break after</label>
      <input type="number" id="long-break" class="form-control" min="1" v-model="longBreakAfter">
      <small class="form-text muted">In pomodoros</small>
    </div>
    <button type="submit" class="btn btn-primary">Start</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      task: '',
      duration: 25,
      shortBreakDuration: 5,
      longBreakDuration: 15,
      longBreakAfter: 4
    }
  },
  methods: {
    submit() {
      this.$emit('submit', {
        task: this.task,
        duration: parseInt(this.duration),
        shortBreakDuration: parseInt(this.shortBreakDuration),
        longBreakDuration: parseInt(this.longBreakDuration),
        longBreakAfter: parseInt(this.longBreakAfter),
      })
    }
  }
}
</script>

<style>
.muted {
  color: #dcdcdc !important;
}
</style>
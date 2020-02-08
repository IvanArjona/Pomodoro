<template>
  <div>
    <StartForm
        v-if="timerCount === 0"
        @submit="startPomodoro($event)"/>
    <template v-else>
      <h2>
        <TimerDescription :pomodoros="timerCount"/>
      </h2>
      <Timer
          :key="timerCount"
          :duration="pomodoroTime"
          :pomodoros="timerCount"
          @next="nextTimer()"/>
    </template>
  </div>
</template>

<script>
import StartForm from './components/StartForm.vue'
import Timer from './components/Timer.vue'
import TimerDescription from './components/TimerDescription.vue'

export default {
  name: 'App',
  data() {
    return {
      task: null,
      duration: null,
      shortBreakDuration: null,
      longBreakDuration: null,
      longBreakAfter: null,
      breakCount: 0,
      timerCount: 0,
      pomodoroTime: null,
    }
  },
  methods: {
    startPomodoro(event) {
      this.task = event.task;
      this.duration = event.duration;
      this.shortBreakDuration = event.shortBreakDuration;
      this.longBreakDuration = event.longBreakDuration;
      this.longBreakAfter = event.longBreakAfter;
      this.nextTimer();
    },
    nextTimer() {
      const timerCount = this.timerCount + 1;
      if (timerCount % 2 != 0) {
        // Pomodoro
        this.pomodoroTime = this.duration;
      } else {
        // Break
        this.pomodoroTime = timerCount / 2 % this.longBreakAfter ? this.shortBreakDuration : this.longBreakDuration;
      }
      this.timerCount = timerCount;
    }
  },
  components: {
    StartForm,
    Timer,
    TimerDescription
  }
}
</script>

<style>

</style>

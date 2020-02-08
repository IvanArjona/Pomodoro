<template>
  <div class="app p-3 d-flex flex-column justify-content-center align-items-center">
    <StartForm
        v-if="timerCount === 0"
        @submit="startPomodoro($event)"/>
    <template v-else>
      <h1 class="task text-center">{{ task }}</h1>
      <h2>
        <TimerDescription :pomodoros="timerCount"/>
      </h2>
      <Timer
          :key="timerCount"
          :duration="pomodoroTime"
          :pomodoros="timerCount"
          @next="nextTimer()"/>
    </template>
    <Footer
        @reset="reset()"/>
  </div>
</template>

<script>
import moment from 'moment';
import StartForm from './components/StartForm.vue'
import Timer from './components/Timer.vue'
import TimerDescription from './components/TimerDescription.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  data() {
    return {
      task: null,
      duration: null,
      shortBreakDuration: null,
      longBreakDuration: null,
      longBreakAfter: null,
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
      this.saveHistory();
    },
    reset() {
      this.timerCount = 0;
    },
    saveHistory() {
      const data = {
        task: this.task,
        duration: this.pomodoroTime,
        start: moment(),
        timer_type_id: this.pomodoros % 2 != 0 ? 1 : (this.pomodoros / 2 % this.longBreakAfter ? 2 : 3)
      }
      fetch('http://localhost:8000/api/timers', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }
      }).then((res) => {
        return res.json();
      });
    }
  },
  components: {
    StartForm,
    Timer,
    TimerDescription,
    Footer,
  }
}
</script>

<style>
body {
  height: 100vh;
}
.app {
  height: 100vh;
  background-color: #C55E5E;
  color: white;
}
.pointer {
  cursor: pointer;
}
.task {
  position: absolute;
  top: 0;
  padding: 1rem;
  width: 100%;
}
</style>

<template>
  <div>
    <p class="countdown">{{ countdown }}</p>
    <button type="submit" class="btn btn-primary" @click.prevent="nextTimer()">
      Start
      <TimerDescription :pomodoros="pomodoros + 1" :longBreakAfter="longBreakAfter"/>
    </button>
  </div>
</template>

<script>
import moment from 'moment';
import TimerDescription from './TimerDescription.vue'

export default {
  name: 'Timer',
  props: {
    duration: Number,
    pomodoros: Number,
    longBreakAfter: Number,
  },
  data() {
    return {
      interval: null,
      countdown: this.duration + ':00',
      ended: false,
    }
  },
  methods: {
    notificationSound() {
      const audioFile = require('../assets/bell.mp3');
      const audio = new Audio(audioFile);
      audio.play();
    },
    startTimer() {
      const start = moment(this.duration, 'm');
      let seconds = start.minutes() * 60;
      this.interval = setInterval(() => {
        this.countdown = start.subtract(1, 'second').format('m:ss');
        seconds--;
        if (seconds === 0) {
          clearInterval(this.interval);
          this.ended = true;
          this.notificationSound();
        }
      }, 1000);
    },
    nextTimer() {
      this.$emit('next');
    }
  },
  mounted() {
    this.startTimer();
  },
  components: {
    TimerDescription
  }
}
</script>

<style scoped>
.countdown {
  font-size: 5rem;
}
</style>

<template>
  <span>{{ description }}</span>
</template>

<script>
export default {
  props: {
    pomodoros: Number,
    longBreakAfter: Number,
  },
  computed: {
    description() {
      if (this.pomodoros % 2 != 0) {
        return 'Work';
      } else {
        return this.pomodoros / 2 % this.longBreakAfter != 0 ? 'Short break' : 'Long break';
      }
    }
  }
}
</script>

<style>

</style>
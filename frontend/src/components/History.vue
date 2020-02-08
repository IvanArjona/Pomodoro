<template>
  <div>
    <span class="pointer" data-toggle="modal" data-target="#history-modal" @click="loadHistory()">History</span>
    <div id="history-modal" class="modal fade" role="dialog">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">History</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <table class="table">
            <thead>
              <tr>
                <th>Task</th>
                <th>Duration</th>
                <th>Start</th>
                <th>Timer</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="timer in history" :key="timer.id">
                <td>{{ timer.task }}</td>
                <td>{{ timer.duration }}</td>
                <td>{{ timer.start }}</td>
                <td>{{ timerType(timer.timer_type_id) }}</td>
              </tr>
            </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import moment from 'moment';

export default {
  data() {
    return {
      history: [],
    }
  },
  methods: {
    loadHistory() {
      fetch('http://localhost:8000/api/timers').then((res) => {
        return res.json();
      }).then((data) => {
        const history = data.map((timer) => {
          if (timer.start) {
            timer.start = moment(timer.start).format('DD/MM/YYYY HH:mm');
          }
          return timer;
        })
        this.history = history;
      });
    },
    timerType(type) {
      return type === 1 ? 'Pomodoro' : (type === 2 ? 'Short break' : 'Long break');
    }
  }
}
</script>

<style>
.modal {
  color: black;
}
</style>
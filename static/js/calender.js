// document.addEventListener('DOMContentLoaded', function() {
//     var calendarEl = document.getElementById('calendar');
//     var today = new Date();

//     var calendar = new FullCalendar.Calendar(calendarEl, {
//         headerToolbar: {
//             left: 'prev,next today',
//             center: 'title',
//             right: 'dayGridMonth,timeGridWeek,timeGridDay,list'
//         },
//         initialDate: today,
//         navLinks: true, // can click day/week names to navigate views 可以單擊日/週名稱來導航視圖
//         selectable: true,
//         selectMirror: true,
//         select: function(arg) {
//             console.log('clicked')
//             var modal = document.getElementById('eventModal')
//             modal.style.display = 'block'
//             calendar.unselect()
//         },
//         // THIS KEY WON'T WORK IN PRODUCTION!!!
//         // To make your own Google API key, follow the directions here:
//         // http://fullcalendar.io/docs/google_calendar/
//         // googleCalendarApiKey: 'AIzaSyCqCxjjLtjbtkX37aOtWB8OfwBLy_6QuYk',

//         // bangladesh Holidays
//         // events: 'bn.bd#holiday@group.v.calendar.google.com',
//         eventClick: function(arg) {
//             if (confirm('Are you sure you want to delete this event?')) {
//                 arg.event.remove()
//             }
//         },
//         editable: true,
//         dayMaxEvents: true, // allow "more" link when too many events 當事件太多時允許“更多”鏈接
//         events: {
//             {
//                 events | safe
//             }
//         },
//         // events: [
//         //   {
//         //     title: 'All Day Event',
//         //     start: '2021-06-26'
//         //   },
//         //   {
//         //     groupId: 999,
//         //     title: 'Repeating Event',
//         //     start: '2020-09-16T16:00:00'
//         //   },
//         //   {
//         //     title: 'Conference',
//         //     start: '2020-09-11',
//         //     end: '2020-09-13'
//         //   },
//         //   {
//         //     title: 'Click for Google',
//         //     url: 'http://google.com/',
//         //     start: '2020-09-28'
//         //   }
//         // ]
//     });

//     calendar.render();
// });
// const closeBtn1 = document.getElementById('modalClose1');
// const closeBtn2 = document.getElementById('modalClose2');
// closeBtn1.addEventListener('click', () => {
//     const eventModal = document.getElementById('eventModal')
//     eventModal.style.display = 'none';
// });
// closeBtn2.addEventListener('click', () => {
//     const eventModal = document.getElementById('eventModal')
//     eventModal.style.display = 'none';
// });

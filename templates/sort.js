var cardContainer = document.querySelector('.card-container');
new Sortable(cardContainer, {
  animation: 150,
  ghostClass: 'sortable-ghost',
  chosenClass: 'sortable-chosen',
  dragClass: 'sortable-drag',
  handle: '.card-header',
  onEnd: function (evt) {
    console.log('Card moved from ' + evt.oldIndex + ' to ' + evt.newIndex);
  }
});
// Bootstrap 4.0.0 does not return focus to the trigger when a modal closes,
// so focus falls to the body and keyboard users lose their place.
// This script stores the element that opened the modal and focuses it again
// after the modal is hidden.
(function ($) {
    'use strict';

    var lastTrigger = null;

    $(document).on('show.bs.modal', '.modal', function (event) {
        lastTrigger = event.relatedTarget || document.activeElement;
    });

    $(document).on('hidden.bs.modal', '.modal', function () {
        if (lastTrigger && typeof lastTrigger.focus === 'function' && document.body.contains(lastTrigger)) {
            lastTrigger.focus();
        }
        lastTrigger = null;
    });
}(jQuery));

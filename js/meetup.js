function jsonp(url, callback) {
    var callbackName = 'jsonp_callback_' + Math.round(100000 * Math.random());
    window[callbackName] = function(data) {
        delete window[callbackName];
        document.body.removeChild(script);
        callback(data);
    };

    var script = document.createElement('script');
    script.src = url + (url.indexOf('?') >= 0 ? '&' : '?') + 'callback=' + callbackName;
    document.body.appendChild(script);
}

const monNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

function processEvents(id, status, resolve, max_events = 0) {
    return events => {
        console.log(events.data);
        var content = "";
        events.data.slice(-max_events).reverse().forEach(function (event) {
            date = new Date(event.local_date);
            content += `
            <li class="items-entry">
                <a href="${event.link}">
                    <div class="items-entry-title">${event.name}</div>
                    <div class="publish-date">${event.local_time} ${monNames[date.getMonth()]} ${date.getDate()}, ${date.getFullYear()}</div>
                </a>
            </li>
            `;
        });
        if (content.length <= 0) {
            content = `<li class="items-entry">There are no ${status} events scheduled... Stay tuned!</li>`;
        }
        resolve(`${content}`);
    }
}

async function getEvents(id, status, max_events = 0) {
    return new Promise(resolve => {
        var url = `https://api.meetup.com/${id}/events?status=${status}`;
        jsonp(url, processEvents(id, status, resolve, max_events));
    });
}

async function eventListUpdater(id, status="upcoming", max_events = 0) {
    var element_id = `${id}-${status}`;
    var list = document.getElementById(element_id);
    list.innerHTML = await getEvents(id, status, max_events);
}

async function updateEventList(id, max_events = 0) {
    eventListUpdater(id, "upcoming", max_events);
    eventListUpdater(id, "past", max_events);
}

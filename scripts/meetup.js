var rp = require('request-promise-native');
var moment = require('moment');
var Twitter = require('twitter-node-client').Twitter;

const twitter_credentials = {
	"consumerKey": process.env.TWITTER_CONSUMER_KEY,
	"consumerSecret": process.env.TWITTER_CONSUMER_SECRET,
	"accessToken": process.env.TWITTER_ACCESS_TOKEN,
	"accessTokenSecret": process.env.TWITTER_ACCESS_TOKEN_SECRET
}

async function get_past_events() {
    const options = {
        uri: 'https://api.meetup.com/python-185/events?desc=true&photo-host=public&page=20&sig_id=12585198&status=past&sig=0f2927de1ea14a1aa98c786fab1aa7739b5eb793',
        json: true
    }
    return rp.get(options);
}

async function get_upcoming_events() {
    const options = {
        uri: 'https://api.meetup.com/python-185/events?desc=true&photo-host=public&page=20&sig_id=12585198&status=upcoming&sig=eaa5e90697efe8c3bc5b2eb3a4014da3912751a3',
        json: true
    }
    return rp.get(options);
}


function get_tweet_for_event(event) {
    const day = moment(event.local_date);
    const day_formatted = day.format('dddd, MMMM Do');
    return `Come to ${event.name}! Next ${day_formatted} at ${event.venue.name}. ${event.link}`;
}


async function send_tweet(tweet, credentials) {
	let error = function (err, response, body) {
        debugger;
        console.log(`ERROR [${err}, ${response}, ${body}]`);
    };
    let success = function (data) {
        console.log('Tweeted: [%s]', data);
    };
    const twitter = new Twitter(credentials);
    const params = {status: tweet};
    twitter.postTweet(params, error, success);
}

async function main(twitter_credentials) {
    const events = await get_past_events();

    const tweets = events.map(get_tweet_for_event);
    const tweet = tweets[0];
    send_tweet(tweet, twitter_credentials);
}

main(twitter_credentials);

var exports = module.exports = {}
exports.get_tweet_for_event = get_tweet_for_event


var expect = require("chai").expect;
var meetup = require("./meetup.js");
 
describe("Meetup", function(){
    it("Should create tweets from events correctly", function() {
        const event = {
            name: 'Python July Meetup',
            local_date: '2018-07-28',
            link: 'https://www.meetup.com/python-185/events/251720316/',
            venue: {
                name: 'TravelPerk'
            }
        };
        const expected = "Come to Python July Meetup! Next Saturday, July 28th at TravelPerk. https://www.meetup.com/python-185/events/251720316/"
        expect(meetup.get_tweet_for_event(event)).to.equal(expected);
    });
 
});

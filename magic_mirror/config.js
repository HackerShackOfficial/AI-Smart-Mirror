/* Magic Mirror Config Sample
/* Magic Mirror Config Sample
 *
 * By Michael Teeuw http://michaelteeuw.nl
 * MIT Licensed.
 */

var config = {
	port: 8080,

	language: 'en',
	timeFormat: 24,
	units: 'metric',

	modules: [
    {
        module: 'aiclient',
        position: 'middle_center' // This can be any of the regions.
    },
    {
    	module: 'aiclientdebugger',
    	position: 'bottom_right'
    }
	]

};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== 'undefined') {module.exports = config;}

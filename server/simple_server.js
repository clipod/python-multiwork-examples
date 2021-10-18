var sleep = require('sleep');

require('http').createServer(function (req, res) {
    console.log('Inside method')
    setTimeout(function() {
        
        res.end('' + process.pid);
    }, 3000);
    
    
}).listen(3000);


var app = {};

app.run = function() {
    app.load.actions();
};

app.load = {
    actions : function () {
         //$('.rc').corners('7px');
    }

};

app.actions = {
    showCoverImage : function () {
        alert('hi');
    }
};

app.ajax = {
};

app.run();


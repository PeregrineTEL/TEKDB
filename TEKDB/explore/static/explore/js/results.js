function resultViewModel() {
  this.results = ko.observableArray([]);
  this.categories = ko.observableArray(['all']);
  this.db_query = ko.observable('*');
  this.filter_categories = ko.observable("");
  this.resultGridArray = ko.computed(function () {
      var rows = [], current = [];
      rows.push(current);
      for (var i = 0; i < this.results().length; i += 1) {
          result = this.results()[i];
          bg_class = (i%2 == 1) ? '' : 'result-alt-highlight';
          current.push({ result: '\
          <a href="' + result.link + '">\
            <div class="row result-desc-row">\
              <div class="col-md-12 col-sm-12 result-desc-col">\
                <div id="result-title_' + i + '" class="result-desc">\
                <h3>' + result.name + '</h3>\
                </div>\
              </div>\
            </div>\
            <div class="row result-img-row">\
              <div class="col-md-12 col-sm-12 result-img-col '+ bg_class + '" style="background-image: url('+ result.image +')">\
                <div class="result-img-content-wrapper">\
                  <p><b>' + result.category_name + '</b></p>\
                  '+ (result.description===null?'':'<p id="result-img_' + i + '">' + result.description + '</p>') + '\
                </div>\
              </div>\
            </div>\
          </a>'});
          if (((i + 1) % 3) === 0) {
              current = [];
              rows.push(current);
          }
      }
      return rows;
  }, this);

  this.loadResults = function() {
    filter_categories = ""
    for (var i=0; i < this.categories().length; i++) {
      category = this.categories()[i];
      filter_categories = filter_categories + "&" + category + "=true";
    }
    this.filter_categories(filter_categories)
    $.ajax(
      {
        url: '/query?query=' + this.db_query() + this.filter_categories(),
        success: function(result) {
          app.resultViewModel.results(result.resultList);
          resize_to_fit();
        },
        error: function(result) {
          window.alert('error!');
        }
      }
    );
    let self = this;
    $('#pagination').pagination({
      dataSource: function(done) {
        $.ajax({
          url: '/query?query=' + self.db_query() + self.filter_categories(),
          success: function(result) {
            done(result.resultList);
            app.resultViewModel.results(result.resultList);
            resize_to_fit();
          },
          error: function(result) {
            window.alert('error!');
          }
        })
      },
      showNavigator: true,
      pageSize: 9,
      locator: 'data',
      callback: function(data, pagination) {
        // template method of yourself
        var html = markupResult(data);
        $('#results-wrap').html(html);
      }
    });
  };

};
app.resultViewModel = new resultViewModel();
ko.applyBindings(app.viewModel);

function resize_to_fit(){
    var titles = $('div.result-desc');
    for (var i = 0; i < titles.length; i++){
      var title = titles[i];
      var id = '#' + title.id;
      resize_title_to_fit($(id));
    }
    var descs = $('div.result-img-content-wrapper');
    for (var i = 0; i < descs.length; i++){
      var desc = descs[i];
      if (desc.children.length > 1) {
        var id = '#' + desc.children[1].id;
        resize_desc_to_fit($(id));
      }
    }
}

function resize_title_to_fit(self){
  var fontsize = self.children().first().css('font-size');
  self.children().first().css('fontSize', parseFloat(fontsize) - 1);
  if(self.height() >= self.parent().height()){
      resize_title_to_fit(self);
  }
}

function resize_desc_to_fit(self){
  if (self.height() >= self.parent().height()-self.siblings().height()){
    text_length = self.text().length;
    self.text(self.text().substring(0,text_length-10) + '...');
    resize_desc_to_fit(self);
  }
}

function markupResult(results) {
  var a = [];
  for (let i = 0; i < results.length; i++) {
    let result = results[i];
    a.push('\
          <div class="col-md-3 col-sm-3 result-cell"><a href="' + result.link + '">\
            <div class="row result-desc-row">\
              <div class="col-md-12 col-sm-12 result-desc-col">\
                <div id="result-title_' + i + '" class="result-desc">\
                <h3>' + result.name + '</h3>\
                </div>\
              </div>\
            </div>\
            <div class="row result-img-row">\
              <div class="col-md-12 col-sm-12 result-img-col '+ bg_class + '" style="background-image: url('+ result.image +')">\
                <div class="result-img-content-wrapper">\
                  <p><b>' + result.category_name + '</b></p>\
                  '+ (result.description===null?'':'<p id="result-img_' + i + '">' + result.description + '</p>') + '\
                </div>\
              </div>\
            </div>\
          </a></div>');
  }
  return a;
}

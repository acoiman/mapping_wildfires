# custom module to create a legend in a Folium Map 

from branca.element import Template, MacroElement

def legend(map):
    
    '''Funtion to create a custom Folium map legend using branca.element class 
    
    Parameters:
    -----------
    map (folium.folium.Map): Folium Map Object

    Returns:
    --------
    no returns
    
    '''
    
    template = """
      {% macro html(this, kwargs) %}

      <!doctype html>
      <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>jQuery UI Draggable - Default functionality</title>
        <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

        <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
        <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

        <script>
        $( function() {
          $( "#maplegend" ).draggable({
                          start: function (event, ui) {
                              $(this).css({
                                  right: "auto",
                                  top: "auto",
                                  bottom: "auto"
                              });
                          }
                      });
      });

        </script>
      </head>
      <body>


      <div id='maplegend' class='maplegend' 
          style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
           border-radius:6px; padding: 2px; font-size:14px; right: 20px; bottom: 20px;'>

        <div class='legend-title'>Legend (draggable!)</div>

        <div class="container">
          <div class="left">
            <p>
              <b>Hotpots 24 hours</b>
            </p>
          </div>
          <div class="right"> 
            <img width="30" height="30" src="https://raw.githubusercontent.com/acoiman/mapping_wildfires/master/icons/fire24.png"  alt="fire 24h"/> 
          </div>
        </div>

        <div class="container">
          <div class="left">
            <p>
              <b>Hotpots 48 hours</b>
            </p>
          </div>
          <div class="right"> 
            <img width="30" height="30" src="https://raw.githubusercontent.com/acoiman/mapping_wildfires/master/icons/fire48.png" alt="fire 48h"/>  
          </div>
        </div>

         <div class="container">
          <div class="left">
            <p>
              <b>Hotpots 7 days</b>
            </p>
          </div>
          <div class="right"> 
            <img width="30" height="30" src="https://raw.githubusercontent.com/acoiman/mapping_wildfires/master/icons/fire7d.png" alt="fire 7d"/>  
          </div>
        </div>
        <br>
      </div>

      </body>
      </html>

      <style type='text/css'>
        .maplegend .legend-title {
          text-align: left;
          font-weight: bold;
          font-size: 90%;
          }
        .maplegend a {
          color: #777;
          }
        .container {
          width:150px;
          display:table;
          margin-bottom: -15px;
          padding: 2px;
        }
          .container > div {
            display:table-cell;
          }
            .container > div p {
              margin:0;
            }
            .container .left {
              text-align:left;
              font-size: 80%;
              color: #777;
              clear: both;
              vertical-align: bottom;
            }
            .container .right {
              text-align:center;
            }
      </style>
      {% endmacro %}"""
    
    macro = MacroElement()
    
    macro._template = Template(template)
    
    map.get_root().add_child(macro)
$(document).ready(function() {
    const songs = [
      { title: "Şarkı 1", lyrics: "<br>Bak bir varmış bir yokmuş eski günlerde <br>Tatlı bir kız yaşarmış Boğaziçi'nde <br>İşte bir sabah erken masal böyle başlamış <br>Delikanlı, genç kıza iskelede rastlamış <br>Bakışmışlar göz göze, gören kimse olmamış <br>Fakat denizle dalga oynamaya başlamış <br>Bak bir varmış bir yokmuş eski günlerde <br>Tatlı bir kız yaşarmış Boğaziçi'nde <br>Delikanlı yaklaşmış Ne kadar güzelsiniz <br>Güzel kız uzaklaşmış Fakat siz de kimsiniz? <br>Ben bir erkek meleğim, bırak yanına geleyim <br>Elimi hiç sürmeden gözlerimle seveyim <br>Bak bir varmış bir yokmuş eski günlerde <br>Tatlı bir kız yaşarmış Boğaziçi'nde <br>Olamaz hayır hayır, annem çok kızar buna <br>Beni kenara ayır, git takıl şuna buna <br>Şayet beni istersen bize yolla anneni <br>Söz veriyorum sana, olacağım gelini <br>Bak bir varmış bir yokmuş eski günlerde <br>Tatlı bir kız yaşarmış Boğaziçi'nde <br>Bak bir varmış bir yokmuş eski günlerde <br>Tatlı bir kız yaşarmış Boğaziçi'nde <br>Oğlan buna inanmış, bir ok gibi yaylanmış <br>Evin yolunu tutup annesine yalvarmış <br>Koş git al kızı bana, delireceğim ana <br>Yoksa oğlun ölecek siyah gözler uğruna <br>Anne atlamış gitmiş içi titreyerekten <br>Güzel kız yağız açmış kapıyı gülerekten <br>Demiş Hanım geç kaldın, bak artık evlendim ben <br>Bekledim de gelmedin, yaya kaldın bu işten <br>Bak bir varmış bir yokmuş eski günlerde <br>Tatlı bir kız yaşarmış Boğaziçi'nde <br>Bak bir varmış bir yokmuş eski günlerde <br>Tatlı bir kız yaşarmış Boğaziçi'nde" },
      { title: "Şarkı 2", lyrics: "Sözler 2..." },

      { title: "Şarkı 3", lyrics: "Sözler 3..." },
      { title: "Şarkı 4", lyrics: "Sözler 2..." },
    
      { title: "Şarkı 1", lyrics: "Sözler 1..." },
      { title: "Şarkı 2", lyrics: "Sözler 2..." },
    
      { title: "Şarkı 1", lyrics: "Sözler 1..." },
      { title: "Şarkı 2", lyrics: "Sözler 2..." }    ];
  
      const songContainer = $('<div class="container"></div>'); // Kapsayıcı bir div eklendi
      $('body').append(songContainer); // Kapsayıcıyı body'e ekle
    
      songs.forEach((song, index) => {
        const songElement = $(`
          <div class="mb-3"> 
            <button class="btn btn-primary btn-block" type="button" data-toggle="collapse" data-target="#collapseLyrics${index}" aria-expanded="false" aria-controls="collapseLyrics${index}">
              ${song.title}
            </button>
            <div class="collapse" id="collapseLyrics${index}">
              <div class="card card-body mt-2">
                ${song.lyrics}
              </div>
            </div>
          </div>
        `);
    
        songContainer.append(songElement); // Şarkı elementini kapsayıcıya ekle
      });
    });
    
"""
Aplikasi Gempa Terkini dari BMKG
Modularisasi Fungtion
"""
import requests
from bs4 import BeautifulSoup

def ekstraksi_data():
    """
    Tanggal : 27 Juli 2022,
    Waktu : 14: 22:29 WIB
    Magnitudo : 4.2
    Kedalaman : 10 km
    Lokasi : 2.04 LS - 124.45 BT
    Pusat gempa berada di laut 171 km barat Sanana
    Dirasakan (Skala MMI): II - III Taliabu
    """
    try:
            content = requests.get('https://www.bmkg.go.id')
    except Exception:
          return None
    if content.status_code == 200:
          soup = BeautifulSoup(content.text, 'html.parser')

          result = soup.find('span', {'class': 'waktu'})
          result =result.text.split(', ')
          tanggal = result[0]
          waktu = result[1]

          result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
          result = soup.findChildren('li')
          print(result)


          #magnitudo =0belum


          hasil = dict()
          hasil['tanggal'] = tanggal #'27 Juli 2022'
          hasil['waktu'] = waktu #'14: 22:29 wib'
          hasil['magnitudo'] =4.2
          hasil['kedalaman'] = 10.0
          hasil['lokasi'] = {'ls': 2.04, 'bt' : - 124.45}
          hasil['pusat'] = 'berada di laut 171 km barat Sanana'
          hasil['dirasakan'] = 'II - III Taliabu'
          return hasil
    else:
          return None

def tampilkan_data(result):
    if result is None:
        print('Tidak Bisa Menemukan Data Gempa terkini')
        return
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")  # cara f" yang di rekomendasikan
    print(f"waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")

#if__name__ =='__main__':
  #  print('ini adalah package gempa terkini')
   # print('hai')



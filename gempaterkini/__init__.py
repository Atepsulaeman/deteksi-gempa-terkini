"""
Aplikasi Gempa Terkini dari BMKG
Modularisasi Fungtion
"""
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

    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
    print(soup.prettify())
    hasil = dict()
    hasil['tanggal'] ='27 Juli 2022'
    hasil['waktu'] = '14: 22:29 wib'
    hasil['magnitudo'] =4.2
    hasil['kedalaman'] = 10.0
    hasil['lokasi'] = {'ls': 2.04, 'bt' : - 124.45}
    hasil['pusat'] = 'berada di laut 171 km barat Sanana'
    hasil['dirasakan'] = 'II - III Taliabu'

    return hasil

def tampilkan_data(result):
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")  # cara f" yang di rekomendasikan
    print(f"waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")



# Enigma
## A Python library for simulating Enigma ciphering machines

This library allows you to encipher (and decipher) [Enigma](https://en.wikipedia.org/wiki/Enigma_machine) messages. It simulates a real Enigma machine and has been tested against real decrypts.

## Example

```python
    from enigma import EnigmaM3

    enigma_machine = EnigmaM3()
    enigma_machine.setup(
        reflector="B",
        rotors="II IV V",
        ring_settings="2 21 12",
        plugboard_pairs="AV BS CG DL FU HZ IN KM OW RX",
        starting_positions="BLA",
    )
    enigma.encode(
        "EDPUD NRGYS ZRCXN UYTPO MRMBO FKTBZ REZKM LXLVE"
        block_size=5,
    )
    "DREIG EHTLA NGSAM ABERS IQERV ORWAE RTSXE INSSI"
```

## Models

It is currently possible to simulate the following Enigma machine types:

|Type|Class|Rotors Used|Rotors Available|Reflectors Available|
| --- | --- | :---: | :---: | :---: |
|[Enigma I](https://en.wikipedia.org/wiki/Enigma_machine#Wehrmacht_Enigma_I_(1930%E2%80%931938)) |`enigma.EnigmaI` |3|5|1|
|[Enigma M3](https://en.wikipedia.org/wiki/Enigma_machine#M3_(1934))|`enigma.EnigmaM3`|3          |8                |3                  |
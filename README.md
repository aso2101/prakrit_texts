# Prakrit Digital Text Project (PDTP)

This is an attempt to collect as much Prakrit literature as possible, using consistent and well-documented reference schemes and a uniform system of transliteration. 

## Project structure

All of the text data will be stored as TEI (P5) XML files. They are in the `tei` directory. (See below for current coverage and desiderata.) The point of using TEI is to be to (a) locate specific passages in the texts (using XPath), and (b) generate a number of secondary formats (e.g., plain text, HTML) if desired. Stylesheets for generating these secondary formats will be provided. Each file contains a `<teiHeader>` element that describes the source(s) on which the digital text is based.

## Transliteration

Prakrit is written with different orthographies in Dēvanāgarī, and it is also transliterated in different ways. This corpus uses the [ISO 15919](https://en.wikipedia.org/wiki/ISO_15919) system for transliteration, which means `ṁ` is used for *anusvāra* rather than `ṃ` (for `e` and `o` see below). These texts **preserve** the orthography of their source editions in the following ways, which are diagnostic of specific scribal or orthographic traditions:
- the quality of vowels is respected (e.g., *benti* or *binti*)
- the use or non-use of *yaśrutiḥ* is respected (e.g., *kayaṁ* or *kaaṁ*)
- the use of dental or retroflex nasals is respected (e.g., *dinnaṁ* or *diṇṇaṁ*)
- the use of question marks, exclamation points, hyphens, and quotation marks is respected.

In other respects the texts have been normalized:
- Generally *parasavarṇa* (class nasals) are used in preference to *anusvāra* (e.g., *intō* rather than *iṁtō*)
- Line-end punctuation in verses has been removed (mostly).
- Numeration at the end of verses has been removed (the numbers are present as attributes in the XML element).
- Sentences are punctuated with periods instead of *daṇḍas.*

The quantity of the vowels *e* and *o* in Prakrit presents difficulties. They are short before double consonants, and generally long elsewhere, but they can often be short in certain morphological environments (e.g., the feminine oblique singular *-āe*, the feminine direct plural *-āo*). The distinction is never made in manuscripts, although sometimes scribes will write *i* or *u* when a short *e* or *o* is meant. In order to preserve metrically-relevant distinctions, we write *ē* and *ō* generally, and *e* and *o* when they appear in a closed syllable (this has not yet been systematically applied), or when they need to be metrically short. We follow the printed editions in making these distinctions.

Non-moraic nasalization of a vowel is marked with a tilde (e.g. एहिँ > ēhĩ).

## Texts and reference systems

The abbreviations mostly follow those of the *Comprehensive and Critical Dictionary of the Prakrit Languages with Special Reference to Jain Literature*.

### Current texts

- **GaüḍVa.x**: *Gaüḍvahaṁ* of Vākpatirāja, *verse* (`//lg[@n='x']`)
- **GāSa.x**: *Gāthāsaptaśatī* of Hāla, *verse* (`//lg[@n='x']`)
- **JōiKa**: *Jyōtiṣkaraṇḍaka* of Pālitta, *verse* (`//lg[@n='x']`)
- **DeNāMā.x.y**: *Dēśināmamālā* of Hēmacandra, *chapter*.*verse* (`//div[@type='adhyāya'][@n='x']/div[@type='gāthā'][@n='y']/quote[@type='base-text']/lg`)
- **Dhutt.x.y**: *Dhūrtākhyāna* of Haribhadra, *chapter*.*verse* (`//div[@type='chapter'][@n='x']/lg[@n='y']`)
- **Līlā.x**: *Līlāvaī* of Kautūhala, *verse* (`//lg[@n='x']`)
- **PāiLaNā.x**: *Pāiyalacchīnāmamālā* of Dhanapāla, *verse* (`//lg[@n='x']`)
- **PaumaCaVi.x.y**: *Paümacariyaṁ* of Vimala Sūri, *chapter*.*verse* (`//div[@type='chapter'][@n='x']/lg[@n='y']`)
- **PrāPi.x.y**: *Prākr̥tapiṅgalam*, *chapter*.*verse* (`//div[@type='chapter'][@n='x']/lg[@n='y']`)
- **SamarāKa.x.y**: *Samarādityakathā* of Haribhadra, *page*.*line* (`//pb[@n='x']`, `//lb[@n='y'])
    - Note that I used the Ahmedabad edition of 1982, so the references in CCDPL (based on Jacobi's edition) will not compute.
- **Sētu.x.y**: *Sētubandha* of Pravarasēna, *chapter*.*verse* (`//div[@type='canto'][@n='x']//lg[@type='stanza'][@n='y']`)
- **SurSuCa.x.y**: *Surasundarīcariya* of Dhanēśvara, *chapter*.*verse* (`//div[@type=' (`//div[@type='paricchēda'][@n='x']/lg[@n='y']`)
- **VajLag.x**: *Vajjālagga* of Jayavallabha, *verse* (`//lg[@n='x']`)
    - Alternatively the reference could take the form *x.y*, where *x* is the *vajjā* and *y* is the verse (`//div[@n='x']/lg[@n='y']`)
- **Vara.x.y.**: *Prākr̥taprakāśa* of Vararuci, *chapter*.*sūtra* (`//div[@type='chapter][@n='x']/ab[@n='y']`)

- Śvētāmbara Jaina Āgamas (based on the files of Muni Deepratnasagar):
    - (06) **Nāyā**: *Nāyādhammakahāō*: numbering based on format
        - **Nāyā.x** (section numbering): *section* (`//div[@type='section'][@n='x']`)
        - **Nāyā.1.x.y** (first *śrutaskandha*): *śrutaskanda*.*adhyayana*.*section* (`//div[@type='śrutaskandha'][@n='1']/div[@type='adhyayana'][@n='x']/div@[type='section][@n='z']`)
        - **Nāyā.2.x.y.z** (second *śrutaskandha*): *śrutaskanda*.*varga*.*adhyayana*.*section* (`//div[@type='śrutaskandha'][@n='2']/div[@type='varga'][@n='x']/div[@type='adhyayana'][@n='y']/div[@type='section][@n='z']`)
	- (34) **Nis**: *Nisīhasuttaṁ*: numbering based on format
        - **Nis.x**: *section* (`//div[@type='section'][@n='x']`)
        - **Nis.x.y**: *chapter*.*section* (`//div[@type='uddēsō'][@n='x']/div[@type='section'][@n='y']`)
    - (35) **Br̥hKapp**: *Br̥hatkalpa*: numbering based on format
        - **Br̥hKapp.x**: *section* (`//div[@type='section'][@n='x']`)
        - **Br̥hKapp.x.y**: *chapter*.*section* (`//div[@type='uddēsō'][@n='x']/div[@type='section'][@n='y']`)
	- (42) **Dasave**: *Daśavaikālikasūtram*:
		- **Dasave.x**: *section* (`//div[@type='section'][@n='x']`)
        - **Dasave.x.y**: *lesson*.*section* (`//div[@type='ajjhayaṇaṁ'][@n='x']/div[@type='section'][@n='y']`)
		- **Dasave.x.y.z**: *lesson*.*chapter*.*section* (`//div[@type='ajjhayaṇaṁ'][@n='x']/div[@type='uddēsō'][@n='y']/div[@type='section'][@n='z']`)
	- (43) **Utt.x.y**: *Uttarādhyayana*, *chapter*.*section* (`//div[@type='ajjhayaṇaṁ'][@n='x']/div[@type='section'][@n='y']`)
    - (44) **Nandī.x**: *Nandīsūtra*, *section* (`//div[@type='section'][@n='x']`)
    - (45) **AṇuŌg.x**: *Anuyōgadvārasūtra*, *section* (`//div[@type='section'][@n='x']`)

### Coming soon

- **Chapp.x**: *Chappaṇṇayagāhāō*, *verse*
- **GāRaKo.x**: *Gāhārayaṇakōsa* of Jinēśvarasūri, *verse*
- **SubhāGāSaṁ.x**: *Subhāsiyagāhāsaṁgaha*, *verse*
- **SubhāPajjSaṁ.x**: *Subhāsiyapajjasaṁgaha*, *verse*
- **Tārā.x**: *Tārāgaṇa* of Bappabhaṭṭi, *verse*

### Desiderata

- **Taraṅga**: Pālitta’s *Taraṅgalōlā* (*Taraṅgavatī*) [ed. H. C. Bhayani 1979]
- **VasuHi**: Saṅghadāsa’s *Vasudēvahiṇḍī*
- **KuvaMā**: Uddyōtana’s *Kuvalayamālā*

## Encoding details

### Languages
It is important to be able to distinguish Sanskrit from Prakrit texts. The postprocessing scripts will assume that *all* text is labeled with a language, in the following manner:

- If an element has an `@xml:lang` attribute, use that.
- Otherwise, get its language from the nearest ancestor with an `@xml:lang` attribute.
	
The `@xml:lang` attribute should use the ISO-639-2 codes:

- `pra-Latn` = Prakrit in the Latin script
- `san-Latn` = Sanskrit in the Latin script
- `hin-Latn` = Hindi in the Latin script
- `eng` = English

## Contributors and funding

Andrew Ollett (University of Chicago)

Funding for the digitization of these texts comes from the following grants:
- NEH HG-5004113 (SARIT: Enriching Digital Texts Collections in Indology)
- The Milton Fund, Harvard University

## License

All of the TEI files include a license. In most, if not all, cases, the text is distributed under a [Creative Commons Attribution-ShareAlike 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/). Please give credit where credit is due if you end up using this data for your own projects.


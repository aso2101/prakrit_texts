# Encoding for Prakrit Texts

## The TEI Header

### The source description

For reporting the printed source on which a TEI document is based, use `biblStruct` in the `sourceDesc` part of the TEI header.

- For titles etc. in languages other than English, make sure you use the `@xml:lang` attribute.
- Titles, names, place names, etc. can be added in multiple languages using `@xml:lang`.
- **Use id numbers.**
  - VIAF for persons
  - WorldCat/OCLC for books
  - Jain E-Library ID numbers

Here is an example:

```xml
<biblStruct>
  <monogr>
    <title level="m" xml:lang="pra-Latn">Sirisivanandivāyagaviraïyapāyayaṭippaṇagasamēyaṁ Thērabhadantasiripālittakāyariyanijjūhiyaṁ Jōisakaraṇḍagaṁ</title>
    <idno type="oclc">245669618</idno>
    <idno type="jainelibrary">001046</idno>
    <editor>
      <persName ref="https://viaf.org/viaf/59522975/">Puṇyavijaya</persName>
    </editor>
    <imprint>
      <publisher>Śrī Mahāvīra Jaina Vidyālaya</publisher>
      <pubPlace>
        <placeName xml:lang="hin-Latn">Bambaī</placeName>
        <placeName xml:lang="eng">Mumbai</placeName>
      </pubPlace>
      <date>1989</date>
    </imprint>
  </monogr>
  <series>
    <title level="s">Jaina-Āgama-Granthamālā</title>
    <biblScope unit="number">17</biblScope>
    <biblScope unit="part">3</biblScope>
  </series>
</biblStruct>
```

## The main text 

The “main text” can often comprise both a “base text” and a “commentary.” It is usually convenient to encode these texts in the same XML document because the structure of the commentary usually follows that of the base text

In such cases, the “base text” is distinguished by being wrapped in the `<quote type="base-text">` attribute.

### Section/chapter headings

The text will often be divided up into sections (using `<div>`). These sections will appear in a table of contents. The processor will look for a title for each section in the following places, by order of preference:

	1. `head[@type='toc']` (be sure to include `@resp` and `@xml:lang` attributes!)
	2. `head/title` (for titles embedded in a header)
	3. the whole `head` element

The sections should also have a number that come from the `@n` attribute of the `div` element. Both the number and the title are used in the table of contents.


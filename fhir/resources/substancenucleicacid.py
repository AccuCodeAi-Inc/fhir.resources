from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceNucleicAcid
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SubstanceNucleicAcid(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Nucleic acids are defined by three distinct elements: the base, sugar and
    linkage. Individual substance/moiety IDs will be created for each of these
    elements. The nucleotide sequence will be always entered in the 5’-3’
    direction.
    """

    __resource_type__ = "SubstanceNucleicAcid"

    areaOfHybridisation: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="areaOfHybridisation",
        title=(
            "The area of hybridisation shall be described if applicable for double "
            "stranded RNA or DNA. The number associated with the subunit followed "
            "by the number associated to the residue shall be specified in "
            "increasing order. The underscore \u201c\u201d shall be used as separator as "
            "follows: \u201cSubunitnumber Residue\u201d"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    areaOfHybridisation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_areaOfHybridisation",
        title="Extension field for ``areaOfHybridisation``.",
    )

    numberOfSubunits: fhirtypes.IntegerType | None = Field(  # type: ignore
        default=None,
        alias="numberOfSubunits",
        title=(
            "The number of linear sequences of nucleotides linked through "
            "phosphodiester bonds shall be described. Subunits would be strands of "
            "nucleic acids that are tightly associated typically through Watson-"
            "Crick base pairing. NOTE: If not specified in the reference source, "
            "the assumption is that there is 1 subunit"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    numberOfSubunits__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_numberOfSubunits",
        title="Extension field for ``numberOfSubunits``.",
    )

    oligoNucleotideType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="oligoNucleotideType",
        title="(TBC)",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    sequenceType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="sequenceType",
        title=(
            "The type of the sequence shall be specified based on a controlled "
            "vocabulary"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    subunit: typing.List[fhirtypes.SubstanceNucleicAcidSubunitType] | None = Field(  # type: ignore
        default=None,
        alias="subunit",
        title=(
            "Subunits are listed in order of decreasing length; sequences of the "
            "same length will be ordered by molecular weight; subunits that have "
            "identical sequences will be repeated multiple times"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceNucleicAcid`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "sequenceType",
            "numberOfSubunits",
            "areaOfHybridisation",
            "oligoNucleotideType",
            "subunit",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceNucleicAcid`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "modifierExtension",
            "sequenceType",
            "numberOfSubunits",
            "areaOfHybridisation",
            "oligoNucleotideType",
            "subunit",
        ]


class SubstanceNucleicAcidSubunit(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Subunits are listed in order of decreasing length; sequences of the same
    length will be ordered by molecular weight; subunits that have identical
    sequences will be repeated multiple times.
    """

    __resource_type__ = "SubstanceNucleicAcidSubunit"

    fivePrime: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="fivePrime",
        title=(
            "The nucleotide present at the 5\u2019 terminal shall be specified based on "
            "a controlled vocabulary. Since the sequence is represented from the 5'"
            " to the 3' end, the 5\u2019 prime nucleotide is the letter at the first "
            "position in the sequence. A separate representation would be redundant"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    length: fhirtypes.IntegerType | None = Field(  # type: ignore
        default=None,
        alias="length",
        title="The length of the sequence shall be captured",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    length__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_length", title="Extension field for ``length``."
    )

    linkage: typing.List[fhirtypes.SubstanceNucleicAcidSubunitLinkageType] | None = Field(  # type: ignore
        default=None,
        alias="linkage",
        title="The linkages between sugar residues will also be captured",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    sequence: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="sequence",
        title=(
            "Actual nucleotide sequence notation from 5' to 3' end using standard "
            "single letter codes. In addition to the base sequence, sugar and type "
            "of phosphate or non-phosphate linkage should also be captured"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_sequence", title="Extension field for ``sequence``."
    )

    sequenceAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        default=None,
        alias="sequenceAttachment",
        title="(TBC)",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    subunit: fhirtypes.IntegerType | None = Field(  # type: ignore
        default=None,
        alias="subunit",
        title=(
            "Index of linear sequences of nucleic acids in order of decreasing "
            "length. Sequences of the same length will be ordered by molecular "
            "weight. Subunits that have identical sequences will be repeated and "
            "have sequential subscripts"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    subunit__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_subunit", title="Extension field for ``subunit``."
    )

    sugar: typing.List[fhirtypes.SubstanceNucleicAcidSubunitSugarType] | None = Field(  # type: ignore
        default=None,
        alias="sugar",
        title="5.3.6.8.1 Sugar ID (Mandatory)",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    threePrime: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="threePrime",
        title=(
            "The nucleotide present at the 3\u2019 terminal shall be specified based on "
            "a controlled vocabulary. Since the sequence is represented from the 5'"
            " to the 3' end, the 5\u2019 prime nucleotide is the letter at the last "
            "position in the sequence. A separate representation would be redundant"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceNucleicAcidSubunit`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "subunit",
            "sequence",
            "length",
            "sequenceAttachment",
            "fivePrime",
            "threePrime",
            "linkage",
            "sugar",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceNucleicAcidSubunit`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "modifierExtension",
            "subunit",
            "sequence",
            "length",
            "sequenceAttachment",
            "fivePrime",
            "threePrime",
            "linkage",
            "sugar",
        ]


class SubstanceNucleicAcidSubunitLinkage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The linkages between sugar residues will also be captured.
    """

    __resource_type__ = "SubstanceNucleicAcidSubunitLinkage"

    connectivity: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="connectivity",
        title=(
            "The entity that links the sugar residues together should also be "
            "captured for nearly all naturally occurring nucleic acid the linkage "
            "is a phosphate group. For many synthetic oligonucleotides "
            "phosphorothioate linkages are often seen. Linkage connectivity is "
            "assumed to be 3\u2019-5\u2019. If the linkage is either 3\u2019-3\u2019 or 5\u2019-5\u2019 this "
            "should be specified"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    connectivity__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_connectivity",
        title="Extension field for ``connectivity``.",
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Each linkage will be registered as a fragment and have an ID",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title=(
            "Each linkage will be registered as a fragment and have at least one "
            "name. A single name shall be assigned to each linkage"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_name", title="Extension field for ``name``."
    )

    residueSite: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="residueSite",
        title="Residues shall be captured as described in 5.3.6.8.3",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    residueSite__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_residueSite", title="Extension field for ``residueSite``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceNucleicAcidSubunitLinkage`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "connectivity",
            "identifier",
            "name",
            "residueSite",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceNucleicAcidSubunitLinkage`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "modifierExtension",
            "connectivity",
            "identifier",
            "name",
            "residueSite",
        ]


class SubstanceNucleicAcidSubunitSugar(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    5.3.6.8.1 Sugar ID (Mandatory).
    """

    __resource_type__ = "SubstanceNucleicAcidSubunitSugar"

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title=(
            "The Substance ID of the sugar or sugar-like component that make up the"
            " nucleotide"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title=(
            "The name of the sugar or sugar-like component that make up the "
            "nucleotide"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_name", title="Extension field for ``name``."
    )

    residueSite: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="residueSite",
        title=(
            "The residues that contain a given sugar will be captured. The order of"
            " given residues will be captured in the 5\u2018-3\u2018direction consistent with"
            " the base sequences listed above"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    residueSite__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_residueSite", title="Extension field for ``residueSite``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceNucleicAcidSubunitSugar`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "name",
            "residueSite",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceNucleicAcidSubunitSugar`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "identifier", "name", "residueSite"]

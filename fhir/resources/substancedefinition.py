from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class SubstanceDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The detailed description of a substance, typically at a level beyond what
    is used for prescribing.
    """

    __resource_type__ = "SubstanceDefinition"

    characterization: typing.List[fhirtypes.SubstanceDefinitionCharacterizationType] | None = Field(  # type: ignore
        default=None,
        alias="characterization",
        title="General specifications for this substance",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    classification: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="classification",
        title=(
            "A categorization, high level e.g. polymer or nucleic acid, or food, "
            "chemical, biological, or lower e.g. polymer linear or branch chain, or"
            " type of impurity"
        ),
        description=(
            "A high level categorization, e.g. polymer or nucleic acid, or food, "
            "chemical, biological, or a lower level such as the general types of "
            "polymer (linear or branch chain) or type of impurity (process related "
            "or contaminant)."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    code: typing.List[fhirtypes.SubstanceDefinitionCodeType] | None = Field(  # type: ignore
        default=None,
        alias="code",
        title="Codes associated with the substance",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title="Textual description of the substance",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_description", title="Extension field for ``description``."
    )

    domain: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="domain",
        title="If the substance applies to human or veterinary use",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    grade: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="grade",
        title=(
            "The quality standard, established benchmark, to which substance "
            "complies (e.g. USP/NF, BP)"
        ),
        description=(
            "The quality standard, established benchmark, to which substance "
            "complies (e.g. USP/NF, Ph. Eur, JP, BP, Company Standard)."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Identifier by which this substance is known",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    informationSource: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="informationSource",
        title="Supporting literature",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Citation"],
        },
    )

    manufacturer: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="manufacturer",
        title="The entity that creates, makes, produces or fabricates the substance",
        description=(
            "The entity that creates, makes, produces or fabricates the substance. "
            "This is a set of potential manufacturers but is not necessarily "
            "comprehensive."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    moiety: typing.List[fhirtypes.SubstanceDefinitionMoietyType] | None = Field(  # type: ignore
        default=None,
        alias="moiety",
        title="Moiety, for structural modifications",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    molecularWeight: typing.List[fhirtypes.SubstanceDefinitionMolecularWeightType] | None = Field(  # type: ignore
        default=None,
        alias="molecularWeight",
        title="The average mass of a molecule of a compound",
        description=(
            "The average mass of a molecule of a compound compared to 1/12 the mass"
            " of carbon 12 and calculated as the sum of the atomic weights of the "
            "constituent atoms."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    name: typing.List[fhirtypes.SubstanceDefinitionNameType] | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="Names applicable to this substance",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        default=None,
        alias="note",
        title="Textual comment about the substance's catalogue or registry record",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    nucleicAcid: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="nucleicAcid",
        title="Data items specific to nucleic acids",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SubstanceNucleicAcid"],
        },
    )

    polymer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="polymer",
        title="Data items specific to polymers",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SubstancePolymer"],
        },
    )

    property: typing.List[fhirtypes.SubstanceDefinitionPropertyType] | None = Field(  # type: ignore
        default=None,
        alias="property",
        title="General specifications for this substance",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    protein: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="protein",
        title="Data items specific to proteins",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SubstanceProtein"],
        },
    )

    referenceInformation: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="referenceInformation",
        title="General information detailing this substance",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SubstanceReferenceInformation"],
        },
    )

    relationship: typing.List[fhirtypes.SubstanceDefinitionRelationshipType] | None = Field(  # type: ignore
        default=None,
        alias="relationship",
        title="A link between this substance and another",
        description=(
            "A link between this substance and another, with details of the "
            "relationship."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    sourceMaterial: fhirtypes.SubstanceDefinitionSourceMaterialType | None = Field(  # type: ignore
        default=None,
        alias="sourceMaterial",
        title="Material or taxonomic/anatomical source",
        description="Material or taxonomic/anatomical source for the substance.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    status: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="Status of substance within the catalogue e.g. active, retired",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    structure: fhirtypes.SubstanceDefinitionStructureType | None = Field(  # type: ignore
        default=None,
        alias="structure",
        title="Structural information",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    supplier: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="supplier",
        title=(
            "An entity that is the source for the substance. It may be different "
            "from the manufacturer"
        ),
        description=(
            "An entity that is the source for the substance. It may be different "
            "from the manufacturer. Supplier is synonymous to a distributor."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="version",
        title="A business level version identifier of the substance",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceDefinition`` according to specification,
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
            "identifier",
            "version",
            "status",
            "classification",
            "domain",
            "grade",
            "description",
            "informationSource",
            "note",
            "manufacturer",
            "supplier",
            "moiety",
            "characterization",
            "property",
            "referenceInformation",
            "molecularWeight",
            "structure",
            "code",
            "name",
            "relationship",
            "nucleicAcid",
            "polymer",
            "protein",
            "sourceMaterial",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceDefinition`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "modifierExtension",
            "identifier",
            "version",
            "status",
            "classification",
            "domain",
            "grade",
            "description",
            "informationSource",
            "note",
            "manufacturer",
            "supplier",
            "moiety",
            "characterization",
            "property",
            "referenceInformation",
            "molecularWeight",
            "structure",
            "code",
            "name",
            "relationship",
            "nucleicAcid",
            "polymer",
            "protein",
            "sourceMaterial",
        ]


class SubstanceDefinitionCharacterization(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    General specifications for this substance.
    """

    __resource_type__ = "SubstanceDefinitionCharacterization"

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title=(
            "The description or justification in support of the interpretation of "
            "the data file"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_description", title="Extension field for ``description``."
    )

    file: typing.List[fhirtypes.AttachmentType] | None = Field(  # type: ignore
        default=None,
        alias="file",
        title=(
            "The data produced by the analytical instrument or a pictorial "
            "representation of that data. Examples: a JCAMP, JDX, or ADX file, or a"
            " chromatogram or spectrum analysis"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    form: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="form",
        title=(
            "Describes the nature of the chemical entity and explains, for "
            "instance, whether this is a base or a salt form"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    technique: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="technique",
        title="The method used to find the characterization e.g. HPLC",
        description=(
            "The method used to elucidate the characterization of the drug "
            "substance. Example: HPLC."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceDefinitionCharacterization`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "technique",
            "form",
            "description",
            "file",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceDefinitionCharacterization`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "technique", "form", "description", "file"]


class SubstanceDefinitionCode(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Codes associated with the substance.
    """

    __resource_type__ = "SubstanceDefinitionCode"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="code",
        title="The specific code",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        default=None,
        alias="note",
        title="Any comment can be provided in this field",
        description="Any comment can be provided in this field, if necessary.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    source: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="source",
        title="Supporting literature",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference"],
        },
    )

    status: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="Status of the code assignment, for example 'provisional', 'approved'",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    statusDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="statusDate",
        title="The date at which the code status was changed",
        description=(
            "The date at which the code status was changed as part of the "
            "terminology maintenance."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceDefinitionCode`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "status",
            "statusDate",
            "note",
            "source",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceDefinitionCode`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "code", "status", "statusDate", "note", "source"]


class SubstanceDefinitionMoiety(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Moiety, for structural modifications.
    """

    __resource_type__ = "SubstanceDefinitionMoiety"

    amountQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="amountQuantity",
        title="Quantitative value for this moiety",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e amount[x]
            "one_of_many": "amount",
            "one_of_many_required": False,
        },
    )

    amountString: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="amountString",
        title="Quantitative value for this moiety",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e amount[x]
            "one_of_many": "amount",
            "one_of_many_required": False,
        },
    )
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_amountString",
        title="Extension field for ``amountString``.",
    )

    identifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Identifier by which this moiety substance is known",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    measurementType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="measurementType",
        title="The measurement type of the quantitative value",
        description=(
            "The measurement type of the quantitative value. In capturing the "
            "actual relative amounts of substances or molecular fragments it may be"
            " necessary to indicate whether the amount refers to, for example, a "
            "mole ratio or weight ratio."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    molecularFormula: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="molecularFormula",
        title="Molecular formula for this moiety (e.g. with the Hill system)",
        description=(
            "Molecular formula for this moiety of this substance, typically using "
            "the Hill system."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    molecularFormula__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_molecularFormula",
        title="Extension field for ``molecularFormula``.",
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="Textual name for this moiety substance",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_name", title="Extension field for ``name``."
    )

    opticalActivity: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="opticalActivity",
        title="Optical activity type",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="role",
        title="Role that the moiety is playing",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    stereochemistry: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="stereochemistry",
        title="Stereochemistry type",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceDefinitionMoiety`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "role",
            "identifier",
            "name",
            "stereochemistry",
            "opticalActivity",
            "molecularFormula",
            "amountQuantity",
            "amountString",
            "measurementType",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceDefinitionMoiety`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "modifierExtension",
            "role",
            "identifier",
            "name",
            "stereochemistry",
            "opticalActivity",
            "molecularFormula",
            "amountQuantity",
            "amountString",
            "measurementType",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"amount": ["amountQuantity", "amountString"]}
        return one_of_many_fields


class SubstanceDefinitionMolecularWeight(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The average mass of a molecule of a compound.
    The average mass of a molecule of a compound compared to 1/12 the mass of
    carbon 12 and calculated as the sum of the atomic weights of the
    constituent atoms.
    """

    __resource_type__ = "SubstanceDefinitionMolecularWeight"

    amount: fhirtypes.QuantityType = Field(  # type: ignore
        default=...,
        alias="amount",
        title="Used to capture quantitative values for a variety of elements",
        description=(
            "Used to capture quantitative values for a variety of elements. If only"
            " limits are given, the arithmetic mean would be the average. If only a"
            " single definite value for a given element is given, it would be "
            "captured in this field."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    method: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="method",
        title="The method by which the weight was determined",
        description="The method by which the molecular weight was determined.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="Type of molecular weight e.g. exact, average, weight average",
        description=(
            "Type of molecular weight such as exact, average (also known as. number"
            " average), weight average."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceDefinitionMolecularWeight`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "method", "type", "amount"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceDefinitionMolecularWeight`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "method", "type", "amount"]


class SubstanceDefinitionName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Names applicable to this substance.
    """

    __resource_type__ = "SubstanceDefinitionName"

    domain: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="domain",
        title=(
            "The use context of this name e.g. as an active ingredient or as a food"
            " colour additive"
        ),
        description=(
            "The use context of this name for example if there is a different name "
            "a drug active ingredient as opposed to a food colour additive."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="jurisdiction",
        title="The jurisdiction where this name applies",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    language: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="language",
        title="Human language that the name is written in",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="The actual name",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_name", title="Extension field for ``name``."
    )

    official: typing.List[fhirtypes.SubstanceDefinitionNameOfficialType] | None = Field(  # type: ignore
        default=None,
        alias="official",
        title="Details of the official nature of this name",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    preferred: bool | None = Field(  # type: ignore
        default=None,
        alias="preferred",
        title="If this is the preferred name for this substance",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    preferred__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_preferred", title="Extension field for ``preferred``."
    )

    source: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="source",
        title="Supporting literature",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference"],
        },
    )

    status: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="The status of the name e.g. 'current', 'proposed'",
        description="The status of the name, for example 'current', 'proposed'.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    synonym: typing.List[fhirtypes.SubstanceDefinitionNameType] | None = Field(  # type: ignore
        default=None,
        alias="synonym",
        title=(
            "A synonym of this particular name, by which the substance is also " "known"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    translation: typing.List[fhirtypes.SubstanceDefinitionNameType] | None = Field(  # type: ignore
        default=None,
        alias="translation",
        title="A translation for this name into another human language",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="Name type e.g. 'systematic',  'scientific, 'brand'",
        description="Name type, for example 'systematic',  'scientific, 'brand'.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceDefinitionName`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "type",
            "status",
            "preferred",
            "language",
            "domain",
            "jurisdiction",
            "synonym",
            "translation",
            "official",
            "source",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceDefinitionName`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "modifierExtension",
            "name",
            "type",
            "status",
            "preferred",
            "language",
            "domain",
            "jurisdiction",
            "synonym",
            "translation",
            "official",
            "source",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext")]
        return required_fields


class SubstanceDefinitionNameOfficial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of the official nature of this name.
    """

    __resource_type__ = "SubstanceDefinitionNameOfficial"

    authority: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="authority",
        title="Which authority uses this official name",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="date",
        title="Date of official name change",
        description="Date of the official name change.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_date", title="Extension field for ``date``."
    )

    status: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="The status of the official name, for example 'draft', 'active'",
        description=(
            "The status of the official name, for example 'draft', 'active', "
            "'retired'."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceDefinitionNameOfficial`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "authority", "status", "date"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceDefinitionNameOfficial`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "authority", "status", "date"]


class SubstanceDefinitionProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    General specifications for this substance.
    """

    __resource_type__ = "SubstanceDefinitionProperty"

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        default=...,
        alias="type",
        title="A code expressing the type of property",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    valueAttachment: fhirtypes.AttachmentType | None = Field(  # type: ignore
        default=None,
        alias="valueAttachment",
        title="A value for the property",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        default=None,
        alias="valueBoolean",
        title="A value for the property",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_valueBoolean",
        title="Extension field for ``valueBoolean``.",
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="valueCodeableConcept",
        title="A value for the property",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDate: fhirtypes.DateType | None = Field(  # type: ignore
        default=None,
        alias="valueDate",
        title="A value for the property",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="valueQuantity",
        title="A value for the property",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceDefinitionProperty`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueCodeableConcept",
            "valueQuantity",
            "valueDate",
            "valueBoolean",
            "valueAttachment",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceDefinitionProperty`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "modifierExtension",
            "type",
            "valueCodeableConcept",
            "valueQuantity",
            "valueDate",
            "valueBoolean",
            "valueAttachment",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "value": [
                "valueAttachment",
                "valueBoolean",
                "valueCodeableConcept",
                "valueDate",
                "valueQuantity",
            ]
        }
        return one_of_many_fields


class SubstanceDefinitionRelationship(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A link between this substance and another.
    A link between this substance and another, with details of the
    relationship.
    """

    __resource_type__ = "SubstanceDefinitionRelationship"

    amountQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="amountQuantity",
        title=(
            "A numeric factor for the relationship, e.g. that a substance salt has "
            "some percentage of active substance in relation to some other"
        ),
        description=(
            "A numeric factor for the relationship, for instance to express that "
            "the salt of a substance has some percentage of the active substance in"
            " relation to some other."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e amount[x]
            "one_of_many": "amount",
            "one_of_many_required": False,
        },
    )

    amountRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        default=None,
        alias="amountRatio",
        title=(
            "A numeric factor for the relationship, e.g. that a substance salt has "
            "some percentage of active substance in relation to some other"
        ),
        description=(
            "A numeric factor for the relationship, for instance to express that "
            "the salt of a substance has some percentage of the active substance in"
            " relation to some other."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e amount[x]
            "one_of_many": "amount",
            "one_of_many_required": False,
        },
    )

    amountString: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="amountString",
        title=(
            "A numeric factor for the relationship, e.g. that a substance salt has "
            "some percentage of active substance in relation to some other"
        ),
        description=(
            "A numeric factor for the relationship, for instance to express that "
            "the salt of a substance has some percentage of the active substance in"
            " relation to some other."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e amount[x]
            "one_of_many": "amount",
            "one_of_many_required": False,
        },
    )
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_amountString",
        title="Extension field for ``amountString``.",
    )

    comparator: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="comparator",
        title=(
            'An operator for the amount, for example "average", "approximately", '
            '"less than"'
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    isDefining: bool | None = Field(  # type: ignore
        default=None,
        alias="isDefining",
        title=(
            "For example where an enzyme strongly bonds with a particular "
            "substance, this is a defining relationship for that enzyme, out of "
            "several possible relationships"
        ),
        description=(
            "For example where an enzyme strongly bonds with a particular "
            "substance, this is a defining relationship for that enzyme, out of "
            "several possible substance relationships."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    isDefining__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_isDefining", title="Extension field for ``isDefining``."
    )

    ratioHighLimitAmount: fhirtypes.RatioType | None = Field(  # type: ignore
        default=None,
        alias="ratioHighLimitAmount",
        title="For use when the numeric has an uncertain range",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    source: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="source",
        title="Supporting literature",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference"],
        },
    )

    substanceDefinitionCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="substanceDefinitionCodeableConcept",
        title=(
            "A pointer to another substance, as a resource or a representational "
            "code"
        ),
        description=(
            "A pointer to another substance, as a resource or just a "
            "representational code."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e substanceDefinition[x]
            "one_of_many": "substanceDefinition",
            "one_of_many_required": False,
        },
    )

    substanceDefinitionReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="substanceDefinitionReference",
        title=(
            "A pointer to another substance, as a resource or a representational "
            "code"
        ),
        description=(
            "A pointer to another substance, as a resource or just a "
            "representational code."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e substanceDefinition[x]
            "one_of_many": "substanceDefinition",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SubstanceDefinition"],
        },
    )

    type: fhirtypes.CodeableConceptType = Field(  # type: ignore
        default=...,
        alias="type",
        title='For example "salt to parent", "active moiety"',
        description=(
            'For example "salt to parent", "active moiety", "starting material", '
            '"polymorph", "impurity of".'
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceDefinitionRelationship`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "substanceDefinitionReference",
            "substanceDefinitionCodeableConcept",
            "type",
            "isDefining",
            "amountQuantity",
            "amountRatio",
            "amountString",
            "ratioHighLimitAmount",
            "comparator",
            "source",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceDefinitionRelationship`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "modifierExtension",
            "substanceDefinitionReference",
            "substanceDefinitionCodeableConcept",
            "type",
            "isDefining",
            "amountQuantity",
            "amountRatio",
            "amountString",
            "ratioHighLimitAmount",
            "comparator",
            "source",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "amount": ["amountQuantity", "amountRatio", "amountString"],
            "substanceDefinition": [
                "substanceDefinitionCodeableConcept",
                "substanceDefinitionReference",
            ],
        }
        return one_of_many_fields


class SubstanceDefinitionSourceMaterial(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Material or taxonomic/anatomical source.
    Material or taxonomic/anatomical source for the substance.
    """

    __resource_type__ = "SubstanceDefinitionSourceMaterial"

    countryOfOrigin: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="countryOfOrigin",
        title="The country or countries where the material is harvested",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    genus: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="genus",
        title=(
            "The genus of an organism e.g. the Latin epithet of the plant/animal "
            "scientific name"
        ),
        description=(
            "The genus of an organism, typically referring to the Latin epithet of "
            "the genus element of the plant/animal scientific name."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    part: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="part",
        title="An anatomical origin of the source material within an organism",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    species: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="species",
        title=(
            "The species of an organism e.g. the Latin epithet of the species of "
            "the plant/animal"
        ),
        description=(
            "The species of an organism, typically referring to the Latin epithet "
            "of the species of the plant/animal."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title=(
            "Classification of the origin of the raw material. e.g. cat hair is an "
            "Animal source type"
        ),
        description=(
            "A classification that provides the origin of the raw material. "
            "Example: cat hair would be an Animal source type."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceDefinitionSourceMaterial`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "genus",
            "species",
            "part",
            "countryOfOrigin",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceDefinitionSourceMaterial`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "modifierExtension",
            "type",
            "genus",
            "species",
            "part",
            "countryOfOrigin",
        ]


class SubstanceDefinitionStructure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Structural information.
    """

    __resource_type__ = "SubstanceDefinitionStructure"

    molecularFormula: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="molecularFormula",
        title=(
            "An expression which states the number and type of atoms present in a "
            "molecule of a substance"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    molecularFormula__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_molecularFormula",
        title="Extension field for ``molecularFormula``.",
    )

    molecularFormulaByMoiety: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="molecularFormulaByMoiety",
        title="Specified per moiety according to the Hill system",
        description=(
            "Specified per moiety according to the Hill system, i.e. first C, then "
            "H, then alphabetical, each moiety separated by a dot."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    molecularFormulaByMoiety__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_molecularFormulaByMoiety",
        title="Extension field for ``molecularFormulaByMoiety``.",
    )

    molecularWeight: fhirtypes.SubstanceDefinitionMolecularWeightType | None = Field(  # type: ignore
        default=None,
        alias="molecularWeight",
        title="The molecular weight or weight range",
        description=(
            "The molecular weight or weight range (for proteins, polymers or "
            "nucleic acids)."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    opticalActivity: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="opticalActivity",
        title="Optical activity type",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    representation: typing.List[fhirtypes.SubstanceDefinitionStructureRepresentationType] | None = Field(  # type: ignore
        default=None,
        alias="representation",
        title="A depiction of the structure of the substance",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    sourceDocument: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="sourceDocument",
        title="Source of information for the structure",
        description="The source of information about the structure.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference"],
        },
    )

    stereochemistry: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="stereochemistry",
        title="Stereochemistry type",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    technique: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="technique",
        title="The method used to find the structure e.g. X-ray, NMR",
        description=(
            "The method used to elucidate the structure of the drug substance. "
            "Examples: X-ray, NMR, Peptide mapping, Ligand binding assay."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceDefinitionStructure`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "stereochemistry",
            "opticalActivity",
            "molecularFormula",
            "molecularFormulaByMoiety",
            "molecularWeight",
            "technique",
            "sourceDocument",
            "representation",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceDefinitionStructure`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "modifierExtension",
            "stereochemistry",
            "opticalActivity",
            "molecularFormula",
            "molecularFormulaByMoiety",
            "molecularWeight",
            "technique",
            "sourceDocument",
            "representation",
        ]


class SubstanceDefinitionStructureRepresentation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A depiction of the structure of the substance.
    """

    __resource_type__ = "SubstanceDefinitionStructureRepresentation"

    document: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="document",
        title=(
            "An attachment with the structural representation e.g. a structure "
            "graphic or AnIML file"
        ),
        description=(
            "An attached file with the structural representation e.g. a molecular "
            "structure graphic of the substance, a JCAMP or AnIML file."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference"],
        },
    )

    format: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="format",
        title=(
            "The format of the representation e.g. InChI, SMILES, MOLFILE (note: "
            "not the physical file format)"
        ),
        description=(
            "The format of the representation e.g. InChI, SMILES, MOLFILE, CDX, "
            "SDF, PDB, mmCIF. The logical content type rather than the physical "
            "file format of a document."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    representation: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="representation",
        title="The structural representation as a text string in a standard format",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    representation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_representation",
        title="Extension field for ``representation``.",
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="The kind of structural representation (e.g. full, partial)",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``SubstanceDefinitionStructureRepresentation`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "representation",
            "format",
            "document",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``SubstanceDefinitionStructureRepresentation`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "type", "representation", "format", "document"]

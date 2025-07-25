from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/GenomicStudy
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class GenomicStudy(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Genomic Study.
    A GenomicStudy is a set of analyses performed to analyze and generate
    genomic data.
    """

    __resource_type__ = "GenomicStudy"

    analysis: typing.List[fhirtypes.GenomicStudyAnalysisType] | None = Field(  # type: ignore
        default=None,
        alias="analysis",
        title="Genomic Analysis Event",
        description=(
            "The details about a specific analysis that was performed in this "
            "GenomicStudy."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="basedOn",
        title="Event resources that the genomic study is based on",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ServiceRequest", "Task"],
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title="Description of the genomic study",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_description", title="Extension field for ``description``."
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="encounter",
        title="The healthcare event with which this genomics study is associated",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Identifiers for this genomic study",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    instantiatesCanonical: fhirtypes.CanonicalType | None = Field(  # type: ignore
        default=None,
        alias="instantiatesCanonical",
        title="The defined protocol that describes the study",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["PlanDefinition"],
        },
    )
    instantiatesCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: fhirtypes.UriType | None = Field(  # type: ignore
        default=None,
        alias="instantiatesUri",
        title=(
            "The URL pointing to an externally maintained protocol that describes "
            "the study"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    instantiatesUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_instantiatesUri",
        title="Extension field for ``instantiatesUri``.",
    )

    interpreter: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="interpreter",
        title="Healthcare professionals who interpreted the genomic study",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        default=None,
        alias="note",
        title="Comments related to the genomic study",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    reason: typing.List[fhirtypes.CodeableReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="reason",
        title="Why the genomic study was performed",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition", "Observation"],
        },
    )

    referrer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="referrer",
        title="Healthcare professional who requested or referred the genomic study",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
        },
    )

    startDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="startDate",
        title="When the genomic study was started",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    startDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_startDate", title="Extension field for ``startDate``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="registered | available | cancelled | entered-in-error | unknown",
        description="The status of the genomic study.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "registered",
                "available",
                "cancelled",
                "entered-in-error",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        default=...,
        alias="subject",
        title="The primary subject of the genomic study",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Group",
                "Substance",
                "BiologicallyDerivedProduct",
                "NutritionProduct",
            ],
        },
    )

    type: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="type",
        title=(
            "The type of the study (e.g., Familial variant segregation, Functional "
            "variation detection, or Gene expression profiling)"
        ),
        description=(
            "The type of the study, e.g., Familial variant segregation, Functional "
            "variation detection, or Gene expression profiling."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``GenomicStudy`` according to specification,
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
            "status",
            "type",
            "subject",
            "encounter",
            "startDate",
            "basedOn",
            "referrer",
            "interpreter",
            "reason",
            "instantiatesCanonical",
            "instantiatesUri",
            "note",
            "description",
            "analysis",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``GenomicStudy`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "modifierExtension",
            "identifier",
            "status",
            "type",
            "subject",
            "encounter",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class GenomicStudyAnalysis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Genomic Analysis Event.
    The details about a specific analysis that was performed in this
    GenomicStudy.
    """

    __resource_type__ = "GenomicStudyAnalysis"

    changeType: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="changeType",
        title=(
            "Type of the genomic changes studied in the analysis (e.g., DNA, RNA, "
            "or AA change)"
        ),
        description=(
            "Type of the genomic changes studied in the analysis, e.g., DNA, RNA, "
            "or amino acid change."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="date",
        title="The date of the analysis event",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_date", title="Extension field for ``date``."
    )

    device: typing.List[fhirtypes.GenomicStudyAnalysisDeviceType] | None = Field(  # type: ignore
        default=None,
        alias="device",
        title=(
            "Devices used for the analysis (e.g., instruments, software), with "
            "settings and parameters"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    focus: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="focus",
        title=(
            "What the genomic analysis is about, when it is not about the subject "
            "of record"
        ),
        description=(
            "The focus of a genomic analysis when it is not the patient of record "
            "representing something or someone associated with the patient such as "
            "a spouse, parent, child, or sibling. For example, in trio testing, the"
            " GenomicStudy.subject would be the child (proband) and the "
            "GenomicStudy.analysis.focus of a specific analysis would be the "
            "parent."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    genomeBuild: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="genomeBuild",
        title="Genome build that is used in this analysis",
        description="The reference genome build that is used in this analysis.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Identifiers for the analysis event",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    input: typing.List[fhirtypes.GenomicStudyAnalysisInputType] | None = Field(  # type: ignore
        default=None,
        alias="input",
        title="Inputs for the analysis event",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    instantiatesCanonical: fhirtypes.CanonicalType | None = Field(  # type: ignore
        default=None,
        alias="instantiatesCanonical",
        title="The defined protocol that describes the analysis",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["PlanDefinition", "ActivityDefinition"],
        },
    )
    instantiatesCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_instantiatesCanonical",
        title="Extension field for ``instantiatesCanonical``.",
    )

    instantiatesUri: fhirtypes.UriType | None = Field(  # type: ignore
        default=None,
        alias="instantiatesUri",
        title=(
            "The URL pointing to an externally maintained protocol that describes "
            "the analysis"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    instantiatesUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_instantiatesUri",
        title="Extension field for ``instantiatesUri``.",
    )

    methodType: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="methodType",
        title=(
            "Type of the methods used in the analysis (e.g., FISH, Karyotyping, " "MSI)"
        ),
        description=(
            "Type of the methods used in the analysis, e.g., Fluorescence in situ "
            "hybridization (FISH), Karyotyping, or Microsatellite instability "
            "testing (MSI)."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        default=None,
        alias="note",
        title="Any notes capture with the analysis event",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    output: typing.List[fhirtypes.GenomicStudyAnalysisOutputType] | None = Field(  # type: ignore
        default=None,
        alias="output",
        title="Outputs for the analysis event",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    performer: typing.List[fhirtypes.GenomicStudyAnalysisPerformerType] | None = Field(  # type: ignore
        default=None,
        alias="performer",
        title="Performer for the analysis event",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    protocolPerformed: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="protocolPerformed",
        title="The protocol that was performed for the analysis event",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Procedure", "Task"],
        },
    )

    regionsCalled: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="regionsCalled",
        title="Genomic regions actually called in the analysis event (BED file)",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference", "Observation"],
        },
    )

    regionsStudied: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="regionsStudied",
        title="The genomic regions to be studied in the analysis (BED file)",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference", "Observation"],
        },
    )

    specimen: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="specimen",
        title="The specimen used in the analysis event",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Specimen"],
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="title",
        title="Name of the analysis event (human friendly)",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_title", title="Extension field for ``title``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``GenomicStudyAnalysis`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "methodType",
            "changeType",
            "genomeBuild",
            "instantiatesCanonical",
            "instantiatesUri",
            "title",
            "focus",
            "specimen",
            "date",
            "note",
            "protocolPerformed",
            "regionsStudied",
            "regionsCalled",
            "input",
            "output",
            "performer",
            "device",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``GenomicStudyAnalysis`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "modifierExtension",
            "identifier",
            "methodType",
            "title",
            "focus",
            "specimen",
        ]


class GenomicStudyAnalysisDevice(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Devices used for the analysis (e.g., instruments, software), with settings
    and parameters.
    """

    __resource_type__ = "GenomicStudyAnalysisDevice"

    device: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="device",
        title="Device used for the analysis",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    function: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="function",
        title="Specific function for the device used for the analysis",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``GenomicStudyAnalysisDevice`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "device", "function"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``GenomicStudyAnalysisDevice`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]


class GenomicStudyAnalysisInput(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Inputs for the analysis event.
    """

    __resource_type__ = "GenomicStudyAnalysisInput"

    file: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="file",
        title="File containing input data",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference"],
        },
    )

    generatedByIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        default=None,
        alias="generatedByIdentifier",
        title=(
            "The analysis event or other GenomicStudy that generated this input " "file"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e generatedBy[x]
            "one_of_many": "generatedBy",
            "one_of_many_required": False,
        },
    )

    generatedByReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="generatedByReference",
        title=(
            "The analysis event or other GenomicStudy that generated this input " "file"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e generatedBy[x]
            "one_of_many": "generatedBy",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["GenomicStudy"],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="Type of input data (e.g., BAM, CRAM, or FASTA)",
        description="Type of input data, e.g., BAM, CRAM, or FASTA.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``GenomicStudyAnalysisInput`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "file",
            "type",
            "generatedByIdentifier",
            "generatedByReference",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``GenomicStudyAnalysisInput`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "file"]

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
            "generatedBy": ["generatedByIdentifier", "generatedByReference"]
        }
        return one_of_many_fields


class GenomicStudyAnalysisOutput(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Outputs for the analysis event.
    """

    __resource_type__ = "GenomicStudyAnalysisOutput"

    file: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="file",
        title="File containing output data",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DocumentReference"],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="Type of output data (e.g., VCF, MAF, or BAM)",
        description="Type of output data, e.g., VCF, MAF, or BAM.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``GenomicStudyAnalysisOutput`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "file", "type"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``GenomicStudyAnalysisOutput`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "file", "type"]


class GenomicStudyAnalysisPerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Performer for the analysis event.
    """

    __resource_type__ = "GenomicStudyAnalysisPerformer"

    actor: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="actor",
        title=(
            "The organization, healthcare professional, or others who participated "
            "in performing this analysis"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "Device",
            ],
        },
    )

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="role",
        title="Role of the actor for this analysis",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``GenomicStudyAnalysisPerformer`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "actor", "role"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``GenomicStudyAnalysisPerformer`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

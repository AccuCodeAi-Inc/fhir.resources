from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/MeasureReport
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MeasureReport(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Results of a measure evaluation.
    The MeasureReport resource contains the results of the calculation of a
    measure; and optionally a reference to the resources involved in that
    calculation.
    """

    __resource_type__ = "MeasureReport"

    dataUpdateType: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="dataUpdateType",
        title="incremental | snapshot",
        description=(
            "Indicates whether the data submitted in a data-exchange report "
            "represents a snapshot or incremental update. A snapshot update "
            "replaces all previously submitted data for the receiver, whereas an "
            "incremental update represents only updated and/or changed data and "
            "should be applied as a differential update to the existing submitted "
            "data for the receiver."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["incremental", "snapshot"],
        },
    )
    dataUpdateType__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_dataUpdateType",
        title="Extension field for ``dataUpdateType``.",
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="date",
        title="When the measure was calculated",
        description="The date this measure was calculated.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_date", title="Extension field for ``date``."
    )

    evaluatedResource: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="evaluatedResource",
        title="What data was used to calculate the measure score",
        description=(
            "Evaluated resources are used to capture what data was involved in the "
            "calculation of a measure. This usage is only allowed for individual "
            "reports to ensure that the size of the MeasureReport resource is "
            "bounded."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    group: typing.List[fhirtypes.MeasureReportGroupType] | None = Field(  # type: ignore
        default=None,
        alias="group",
        title="Measure results for each group",
        description=(
            "The results of the calculation, one for each population group in the "
            "measure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Additional identifier for the MeasureReport",
        description=(
            "A formal identifier that is used to identify this MeasureReport when "
            "it is represented in other formats or referenced in a specification, "
            "model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    improvementNotation: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="improvementNotation",
        title="increase | decrease",
        description=(
            "Whether improvement in the measure is noted by an increase or decrease"
            " in the measure score."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    inputParameters: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="inputParameters",
        title="What parameters were provided to the report",
        description=(
            "A reference to a Parameters resource (typically represented using a "
            "contained resource) that represents any input parameters that were "
            "provided to the operation that generated the report."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Parameters"],
        },
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="location",
        title="Where the reported data is from",
        description="A reference to the location for which the data is being reported.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    measure: fhirtypes.CanonicalType | None = Field(  # type: ignore
        default=None,
        alias="measure",
        title="What measure was calculated",
        description="A reference to the Measure that was calculated to produce this report.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Measure"],
        },
    )
    measure__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_measure", title="Extension field for ``measure``."
    )

    period: fhirtypes.PeriodType = Field(  # type: ignore
        default=...,
        alias="period",
        title="What period the report covers",
        description="The reporting period for which the report was calculated.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    reporter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="reporter",
        title="Who is reporting the data",
        description="The individual or organization that is reporting the data.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "Group",
            ],
        },
    )

    reportingVendor: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="reportingVendor",
        title="What vendor prepared the data",
        description=(
            "A reference to the vendor who queried the data, calculated results "
            "and/or generated the report. The \u2018reporting vendor\u2019 is intended to "
            "represent the submitting entity when it is not the same as the "
            "reporting entity. This extension is used when the Receiver is "
            "interested in getting vendor information in the report."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    scoring: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="scoring",
        title="What scoring method (e.g. proportion, ratio, continuous-variable)",
        description=(
            "Indicates how the calculation is performed for the measure, including "
            "proportion, ratio, continuous-variable, and cohort. The value set is "
            "extensible, allowing additional measure scoring types to be "
            "represented. It is expected to be the same as the scoring element on "
            "the referenced Measure."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="complete | pending | error",
        description=(
            "The MeasureReport status. No data will be available until the "
            "MeasureReport status is complete."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["complete", "pending", "error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="subject",
        title="What individual(s) the report is for",
        description=(
            "Optional subject identifying the individual or individuals the report "
            "is for."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CareTeam",
                "Device",
                "Group",
                "HealthcareService",
                "Location",
                "Organization",
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
            ],
        },
    )

    supplementalData: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="supplementalData",
        title="Additional information collected for the report",
        description=(
            "A reference to a Resource that represents additional information "
            "collected for the report. If the value of the supplemental data is not"
            " a Resource (i.e. evaluating the supplementalData expression for this "
            "case in the measure results in a value that is not a FHIR Resource), "
            "it is reported as a reference to a contained Observation resource."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="individual | subject-list | summary | data-exchange",
        description=(
            "The type of measure report. This may be an individual report, which "
            "provides the score for the measure for an individual member of the "
            "population; a subject-listing, which returns the list of members that "
            "meet the various criteria in the measure; a summary report, which "
            "returns a population count for each of the criteria in the measure; or"
            " a data-collection, which enables the MeasureReport to be used to "
            "exchange the data-of-interest for a quality measure."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["individual", "subject-list", "summary", "data-exchange"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``MeasureReport`` according to specification,
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
            "dataUpdateType",
            "measure",
            "subject",
            "date",
            "reporter",
            "reportingVendor",
            "location",
            "period",
            "inputParameters",
            "scoring",
            "improvementNotation",
            "group",
            "supplementalData",
            "evaluatedResource",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``MeasureReport`` according to specification,
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
            "dataUpdateType",
            "measure",
            "subject",
            "date",
            "reporter",
            "period",
            "scoring",
            "improvementNotation",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext"), ("type", "type__ext")]
        return required_fields


class MeasureReportGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Measure results for each group.
    The results of the calculation, one for each population group in the
    measure.
    """

    __resource_type__ = "MeasureReportGroup"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="code",
        title="Meaning of the group",
        description=(
            "The meaning of the population group as defined in the measure "
            "definition."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    linkId: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="linkId",
        title="Pointer to specific group from Measure",
        description=(
            "The group from the Measure that corresponds to this group in the "
            "MeasureReport resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_linkId", title="Extension field for ``linkId``."
    )

    measureScoreCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="measureScoreCodeableConcept",
        title="What score this group achieved",
        description=(
            "The measure score for this population group, calculated as appropriate"
            " for the measure type and scoring method, and based on the contents of"
            " the populations defined in the group."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e measureScore[x]
            "one_of_many": "measureScore",
            "one_of_many_required": False,
        },
    )

    measureScoreDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="measureScoreDateTime",
        title="What score this group achieved",
        description=(
            "The measure score for this population group, calculated as appropriate"
            " for the measure type and scoring method, and based on the contents of"
            " the populations defined in the group."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e measureScore[x]
            "one_of_many": "measureScore",
            "one_of_many_required": False,
        },
    )
    measureScoreDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_measureScoreDateTime",
        title="Extension field for ``measureScoreDateTime``.",
    )

    measureScoreDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        default=None,
        alias="measureScoreDuration",
        title="What score this group achieved",
        description=(
            "The measure score for this population group, calculated as appropriate"
            " for the measure type and scoring method, and based on the contents of"
            " the populations defined in the group."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e measureScore[x]
            "one_of_many": "measureScore",
            "one_of_many_required": False,
        },
    )

    measureScorePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        default=None,
        alias="measureScorePeriod",
        title="What score this group achieved",
        description=(
            "The measure score for this population group, calculated as appropriate"
            " for the measure type and scoring method, and based on the contents of"
            " the populations defined in the group."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e measureScore[x]
            "one_of_many": "measureScore",
            "one_of_many_required": False,
        },
    )

    measureScoreQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="measureScoreQuantity",
        title="What score this group achieved",
        description=(
            "The measure score for this population group, calculated as appropriate"
            " for the measure type and scoring method, and based on the contents of"
            " the populations defined in the group."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e measureScore[x]
            "one_of_many": "measureScore",
            "one_of_many_required": False,
        },
    )

    measureScoreRange: fhirtypes.RangeType | None = Field(  # type: ignore
        default=None,
        alias="measureScoreRange",
        title="What score this group achieved",
        description=(
            "The measure score for this population group, calculated as appropriate"
            " for the measure type and scoring method, and based on the contents of"
            " the populations defined in the group."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e measureScore[x]
            "one_of_many": "measureScore",
            "one_of_many_required": False,
        },
    )

    population: typing.List[fhirtypes.MeasureReportGroupPopulationType] | None = Field(  # type: ignore
        default=None,
        alias="population",
        title="The populations in the group",
        description=(
            "The populations that make up the population group, one for each type "
            "of population appropriate for the measure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    stratifier: typing.List[fhirtypes.MeasureReportGroupStratifierType] | None = Field(  # type: ignore
        default=None,
        alias="stratifier",
        title="Stratification results",
        description=(
            "When a measure includes multiple stratifiers, there will be a "
            "stratifier group for each stratifier defined by the measure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    subject: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="subject",
        title="What individual(s) the report is for",
        description=(
            "Optional subject identifying the individual or individuals the report "
            "is for."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "CareTeam",
                "Device",
                "Group",
                "HealthcareService",
                "Location",
                "Organization",
                "Patient",
                "Practitioner",
                "PractitionerRole",
                "RelatedPerson",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``MeasureReportGroup`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "linkId",
            "code",
            "subject",
            "population",
            "measureScoreQuantity",
            "measureScoreDateTime",
            "measureScoreCodeableConcept",
            "measureScorePeriod",
            "measureScoreRange",
            "measureScoreDuration",
            "stratifier",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``MeasureReportGroup`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "modifierExtension",
            "code",
            "subject",
            "measureScoreQuantity",
            "measureScoreDateTime",
            "measureScoreCodeableConcept",
            "measureScorePeriod",
            "measureScoreRange",
            "measureScoreDuration",
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
            "measureScore": [
                "measureScoreCodeableConcept",
                "measureScoreDateTime",
                "measureScoreDuration",
                "measureScorePeriod",
                "measureScoreQuantity",
                "measureScoreRange",
            ]
        }
        return one_of_many_fields


class MeasureReportGroupPopulation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The populations in the group.
    The populations that make up the population group, one for each type of
    population appropriate for the measure.
    """

    __resource_type__ = "MeasureReportGroupPopulation"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="code",
        title=(
            "initial-population | numerator | numerator-exclusion | denominator | "
            "denominator-exclusion | denominator-exception | measure-population | "
            "measure-population-exclusion | measure-observation"
        ),
        description="The type of the population.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    count: fhirtypes.IntegerType | None = Field(  # type: ignore
        default=None,
        alias="count",
        title="Size of the population",
        description="The number of members of the population.",
        json_schema_extra={
            "element_property": True,
        },
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_count", title="Extension field for ``count``."
    )

    linkId: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="linkId",
        title="Pointer to specific population from Measure",
        description=(
            "The population from the Measure that corresponds to this population in"
            " the MeasureReport resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_linkId", title="Extension field for ``linkId``."
    )

    subjectReport: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="subjectReport",
        title="For subject-list reports, a subject result in this population",
        description=(
            "A reference to an individual level MeasureReport resource for a member"
            " of the population."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MeasureReport"],
        },
    )

    subjectResults: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="subjectResults",
        title="For subject-list reports, the subject results in this population",
        description=(
            "This element refers to a List of individual level MeasureReport "
            "resources, one for each subject in this population."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["List"],
        },
    )

    subjects: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="subjects",
        title="What individual(s) in the population",
        description=(
            "Optional Group identifying the individuals that make up the " "population."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``MeasureReportGroupPopulation`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "linkId",
            "code",
            "count",
            "subjectResults",
            "subjectReport",
            "subjects",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``MeasureReportGroupPopulation`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "code"]


class MeasureReportGroupStratifier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stratification results.
    When a measure includes multiple stratifiers, there will be a stratifier
    group for each stratifier defined by the measure.
    """

    __resource_type__ = "MeasureReportGroupStratifier"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="code",
        title="What stratifier of the group",
        description="The meaning of this stratifier, as defined in the measure definition.",
        json_schema_extra={
            "element_property": True,
        },
    )

    linkId: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="linkId",
        title="Pointer to specific stratifier from Measure",
        description=(
            "The stratifier from the Measure that corresponds to this stratifier in"
            " the MeasureReport resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_linkId", title="Extension field for ``linkId``."
    )

    stratum: typing.List[fhirtypes.MeasureReportGroupStratifierStratumType] | None = Field(  # type: ignore
        default=None,
        alias="stratum",
        title=(
            "Stratum results, one for each unique value, or set of values, in the "
            "stratifier, or stratifier components"
        ),
        description=(
            "This element contains the results for a single stratum within the "
            "stratifier. For example, when stratifying on administrative gender, "
            "there will be four strata, one for each possible gender value."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``MeasureReportGroupStratifier`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "linkId", "code", "stratum"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``MeasureReportGroupStratifier`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]


class MeasureReportGroupStratifierStratum(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stratum results, one for each unique value, or set of values, in the
    stratifier, or stratifier components.
    This element contains the results for a single stratum within the
    stratifier. For example, when stratifying on administrative gender, there
    will be four strata, one for each possible gender value.
    """

    __resource_type__ = "MeasureReportGroupStratifierStratum"

    component: typing.List[fhirtypes.MeasureReportGroupStratifierStratumComponentType] | None = Field(  # type: ignore
        default=None,
        alias="component",
        title="Stratifier component values",
        description="A stratifier component value.",
        json_schema_extra={
            "element_property": True,
        },
    )

    measureScoreCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="measureScoreCodeableConcept",
        title="What score this stratum achieved",
        description=(
            "The measure score for this stratum, calculated as appropriate for the "
            "measure type and scoring method, and based on only the members of this"
            " stratum."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e measureScore[x]
            "one_of_many": "measureScore",
            "one_of_many_required": False,
        },
    )

    measureScoreDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="measureScoreDateTime",
        title="What score this stratum achieved",
        description=(
            "The measure score for this stratum, calculated as appropriate for the "
            "measure type and scoring method, and based on only the members of this"
            " stratum."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e measureScore[x]
            "one_of_many": "measureScore",
            "one_of_many_required": False,
        },
    )
    measureScoreDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_measureScoreDateTime",
        title="Extension field for ``measureScoreDateTime``.",
    )

    measureScoreDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        default=None,
        alias="measureScoreDuration",
        title="What score this stratum achieved",
        description=(
            "The measure score for this stratum, calculated as appropriate for the "
            "measure type and scoring method, and based on only the members of this"
            " stratum."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e measureScore[x]
            "one_of_many": "measureScore",
            "one_of_many_required": False,
        },
    )

    measureScorePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        default=None,
        alias="measureScorePeriod",
        title="What score this stratum achieved",
        description=(
            "The measure score for this stratum, calculated as appropriate for the "
            "measure type and scoring method, and based on only the members of this"
            " stratum."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e measureScore[x]
            "one_of_many": "measureScore",
            "one_of_many_required": False,
        },
    )

    measureScoreQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="measureScoreQuantity",
        title="What score this stratum achieved",
        description=(
            "The measure score for this stratum, calculated as appropriate for the "
            "measure type and scoring method, and based on only the members of this"
            " stratum."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e measureScore[x]
            "one_of_many": "measureScore",
            "one_of_many_required": False,
        },
    )

    measureScoreRange: fhirtypes.RangeType | None = Field(  # type: ignore
        default=None,
        alias="measureScoreRange",
        title="What score this stratum achieved",
        description=(
            "The measure score for this stratum, calculated as appropriate for the "
            "measure type and scoring method, and based on only the members of this"
            " stratum."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e measureScore[x]
            "one_of_many": "measureScore",
            "one_of_many_required": False,
        },
    )

    population: typing.List[fhirtypes.MeasureReportGroupStratifierStratumPopulationType] | None = Field(  # type: ignore
        default=None,
        alias="population",
        title="Population results in this stratum",
        description=(
            "The populations that make up the stratum, one for each type of "
            "population appropriate to the measure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    valueBoolean: bool | None = Field(  # type: ignore
        default=None,
        alias="valueBoolean",
        title="The stratum value, e.g. male",
        description=(
            "The value for this stratum, expressed as a CodeableConcept. When "
            "defining stratifiers on complex values, the value must be rendered "
            "such that the value for each stratum within the stratifier is unique."
        ),
        json_schema_extra={
            "element_property": True,
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
        title="The stratum value, e.g. male",
        description=(
            "The value for this stratum, expressed as a CodeableConcept. When "
            "defining stratifiers on complex values, the value must be rendered "
            "such that the value for each stratum within the stratifier is unique."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="valueQuantity",
        title="The stratum value, e.g. male",
        description=(
            "The value for this stratum, expressed as a CodeableConcept. When "
            "defining stratifiers on complex values, the value must be rendered "
            "such that the value for each stratum within the stratifier is unique."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueRange: fhirtypes.RangeType | None = Field(  # type: ignore
        default=None,
        alias="valueRange",
        title="The stratum value, e.g. male",
        description=(
            "The value for this stratum, expressed as a CodeableConcept. When "
            "defining stratifiers on complex values, the value must be rendered "
            "such that the value for each stratum within the stratifier is unique."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="valueReference",
        title="The stratum value, e.g. male",
        description=(
            "The value for this stratum, expressed as a CodeableConcept. When "
            "defining stratifiers on complex values, the value must be rendered "
            "such that the value for each stratum within the stratifier is unique."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``MeasureReportGroupStratifierStratum`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "valueCodeableConcept",
            "valueBoolean",
            "valueQuantity",
            "valueRange",
            "valueReference",
            "component",
            "population",
            "measureScoreQuantity",
            "measureScoreDateTime",
            "measureScoreCodeableConcept",
            "measureScorePeriod",
            "measureScoreRange",
            "measureScoreDuration",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``MeasureReportGroupStratifierStratum`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

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
            "measureScore": [
                "measureScoreCodeableConcept",
                "measureScoreDateTime",
                "measureScoreDuration",
                "measureScorePeriod",
                "measureScoreQuantity",
                "measureScoreRange",
            ],
            "value": [
                "valueBoolean",
                "valueCodeableConcept",
                "valueQuantity",
                "valueRange",
                "valueReference",
            ],
        }
        return one_of_many_fields


class MeasureReportGroupStratifierStratumComponent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Stratifier component values.
    A stratifier component value.
    """

    __resource_type__ = "MeasureReportGroupStratifierStratumComponent"

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        default=...,
        alias="code",
        title="What stratifier component of the group",
        description="The code for the stratum component value.",
        json_schema_extra={
            "element_property": True,
        },
    )

    linkId: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="linkId",
        title="Pointer to specific stratifier component from Measure",
        description=(
            "The stratifier component from the Measure that corresponds to this "
            "stratifier component in the MeasureReport resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_linkId", title="Extension field for ``linkId``."
    )

    valueBoolean: bool | None = Field(  # type: ignore
        default=None,
        alias="valueBoolean",
        title="The stratum component value, e.g. male",
        description="The stratum component value.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
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
        title="The stratum component value, e.g. male",
        description="The stratum component value.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="valueQuantity",
        title="The stratum component value, e.g. male",
        description="The stratum component value.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueRange: fhirtypes.RangeType | None = Field(  # type: ignore
        default=None,
        alias="valueRange",
        title="The stratum component value, e.g. male",
        description="The stratum component value.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="valueReference",
        title="The stratum component value, e.g. male",
        description="The stratum component value.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``MeasureReportGroupStratifierStratumComponent`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "linkId",
            "code",
            "valueCodeableConcept",
            "valueBoolean",
            "valueQuantity",
            "valueRange",
            "valueReference",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``MeasureReportGroupStratifierStratumComponent`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

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
                "valueBoolean",
                "valueCodeableConcept",
                "valueQuantity",
                "valueRange",
                "valueReference",
            ]
        }
        return one_of_many_fields


class MeasureReportGroupStratifierStratumPopulation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Population results in this stratum.
    The populations that make up the stratum, one for each type of population
    appropriate to the measure.
    """

    __resource_type__ = "MeasureReportGroupStratifierStratumPopulation"

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="code",
        title=(
            "initial-population | numerator | numerator-exclusion | denominator | "
            "denominator-exclusion | denominator-exception | measure-population | "
            "measure-population-exclusion | measure-observation"
        ),
        description="The type of the population.",
        json_schema_extra={
            "element_property": True,
        },
    )

    count: fhirtypes.IntegerType | None = Field(  # type: ignore
        default=None,
        alias="count",
        title="Size of the population",
        description="The number of members of the population in this stratum.",
        json_schema_extra={
            "element_property": True,
        },
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_count", title="Extension field for ``count``."
    )

    linkId: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="linkId",
        title="Pointer to specific population from Measure",
        description=(
            "The population from the Measure that corresponds to this population in"
            " the MeasureReport resource."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_linkId", title="Extension field for ``linkId``."
    )

    subjectReport: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="subjectReport",
        title="For subject-list reports, a subject result in this population",
        description=(
            "A reference to an individual level MeasureReport resource for a member"
            " of the population."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MeasureReport"],
        },
    )

    subjectResults: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="subjectResults",
        title="For subject-list reports, the subject results in this population",
        description=(
            "This element refers to a List of individual level MeasureReport "
            "resources, one for each subject in this population in this stratum."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["List"],
        },
    )

    subjects: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="subjects",
        title="What individual(s) in the population",
        description=(
            "Optional Group identifying the individuals that make up the " "population."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``MeasureReportGroupStratifierStratumPopulation`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "linkId",
            "code",
            "count",
            "subjectResults",
            "subjectReport",
            "subjects",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``MeasureReportGroupStratifierStratumPopulation`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ResearchStudy
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ResearchStudy(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Investigation to increase healthcare-related patient-independent knowledge.
    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques.  A ResearchStudy
    involves the gathering of information about human or animal subjects.
    """

    __resource_type__ = "ResearchStudy"

    arm: typing.List[fhirtypes.ResearchStudyArmType] | None = Field(  # type: ignore
        default=None,
        alias="arm",
        title="Defined path through the study for a subject",
        description=(
            "Describes an expected sequence of events for one of the participants "
            "of a study.  E.g. Exposure to drug A, wash-out, exposure to drug B, "
            "wash-out, follow-up."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="category",
        title="Classifications for the study",
        description=(
            "Codes categorizing the type of study such as investigational vs. "
            "observational, type of blinding, type of randomization, safety vs. "
            "efficacy, etc."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    condition: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="condition",
        title="Condition being studied",
        description=(
            "The condition that is the focus of the study.  For example, In a study"
            " to examine risk factors for Lupus, might have as an inclusion "
            'criterion "healthy volunteer", but the target condition code would be '
            "a Lupus SNOMED code."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    contact: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        default=None,
        alias="contact",
        title="Contact details for the study",
        description=(
            "Contact details to assist a user in learning more about or engaging "
            "with the study."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title="What this is study doing",
        description="A full description of how the study is being conducted.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_description", title="Extension field for ``description``."
    )

    enrollment: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="enrollment",
        title="Inclusion & exclusion criteria",
        description=(
            "Reference to a Group that defines the criteria for and quantity of "
            'subjects participating in the study.  E.g. " 200 female Europeans '
            'between the ages of 20 and 45 with early onset diabetes".'
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group"],
        },
    )

    focus: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="focus",
        title="Drugs, devices, etc. under study",
        description=(
            "The medication(s), food(s), therapy(ies), device(s) or other concerns "
            "or interventions that the study is seeking to gain more information "
            "about."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Business Identifier for study",
        description=(
            "Identifiers assigned to this research study by the sponsor or other "
            "systems."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    keyword: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="keyword",
        title="Used to search for the study",
        description="Key terms to aid in searching for or filtering the study.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    location: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="location",
        title="Geographic region(s) for study",
        description=(
            "Indicates a country, state or other region where the study is taking "
            "place."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        default=None,
        alias="note",
        title="Comments made about the study",
        description=(
            "Comments made about the study by the performer, subject or other "
            "participants."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    objective: typing.List[fhirtypes.ResearchStudyObjectiveType] | None = Field(  # type: ignore
        default=None,
        alias="objective",
        title="A goal for the study",
        description=(
            "A goal that the study is aiming to achieve in terms of a scientific "
            "question to be answered by the analysis of data collected during the "
            "study."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    partOf: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="partOf",
        title="Part of larger study",
        description=(
            "A larger research study of which this particular study is a component "
            "or step."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ResearchStudy"],
        },
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        default=None,
        alias="period",
        title="When the study began and ended",
        description=(
            "Identifies the start date and the expected (or actual, depending on "
            "status) end date for the study."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    phase: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="phase",
        title=(
            "n-a | early-phase-1 | phase-1 | phase-1-phase-2 | phase-2 | "
            "phase-2-phase-3 | phase-3 | phase-4"
        ),
        description=(
            "The stage in the progression of a therapy from initial experimental "
            "use in humans in clinical trials to post-market evaluation."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    primaryPurposeType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="primaryPurposeType",
        title=(
            "treatment | prevention | diagnostic | supportive-care | screening | "
            "health-services-research | basic-science | device-feasibility"
        ),
        description=(
            "The type of study based upon the intent of the study's activities. A "
            "classification of the intent of the study."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    principalInvestigator: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="principalInvestigator",
        title="Researcher who oversees multiple aspects of the study",
        description=(
            "A researcher in a study who oversees multiple aspects of the study, "
            "such as concept development, protocol writing, protocol submission for"
            " IRB approval, participant recruitment, informed consent, data "
            "collection, analysis, interpretation and presentation."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
        },
    )

    protocol: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="protocol",
        title="Steps followed in executing study",
        description=(
            "The set of steps expected to be performed as part of the execution of "
            "the study."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["PlanDefinition"],
        },
    )

    reasonStopped: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="reasonStopped",
        title=(
            "accrual-goal-met | closed-due-to-toxicity | closed-due-to-lack-of-"
            "study-progress | temporarily-closed-per-study-design"
        ),
        description=(
            "A description and/or code explaining the premature termination of the "
            "study."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        default=None,
        alias="relatedArtifact",
        title="References and dependencies",
        description="Citations, references and other related documents.",
        json_schema_extra={
            "element_property": True,
        },
    )

    site: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="site",
        title="Facility where study activities are conducted",
        description="A facility in which study activities are conducted.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    sponsor: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="sponsor",
        title="Organization that initiates and is legally responsible for the study",
        description=(
            "An organization that initiates the investigation and is legally "
            "responsible for the study."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title=(
            "active | administratively-completed | approved | closed-to-accrual | "
            "closed-to-accrual-and-intervention | completed | disapproved | in-"
            "review | temporarily-closed-to-accrual | temporarily-closed-to-"
            "accrual-and-intervention | withdrawn"
        ),
        description="The current state of the study.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "active",
                "administratively-completed",
                "approved",
                "closed-to-accrual",
                "closed-to-accrual-and-intervention",
                "completed",
                "disapproved",
                "in-review",
                "temporarily-closed-to-accrual",
                "temporarily-closed-to-accrual-and-intervention",
                "withdrawn",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="title",
        title="Name for this study",
        description="A short, descriptive user-friendly label for the study.",
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
        ``ResearchStudy`` according to specification,
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
            "title",
            "protocol",
            "partOf",
            "status",
            "primaryPurposeType",
            "phase",
            "category",
            "focus",
            "condition",
            "contact",
            "relatedArtifact",
            "keyword",
            "location",
            "description",
            "enrollment",
            "period",
            "sponsor",
            "principalInvestigator",
            "site",
            "reasonStopped",
            "note",
            "arm",
            "objective",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``ResearchStudy`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "identifier",
            "title",
            "protocol",
            "partOf",
            "status",
            "primaryPurposeType",
            "phase",
            "category",
            "focus",
            "condition",
            "contact",
            "keyword",
            "location",
            "enrollment",
            "period",
            "sponsor",
            "principalInvestigator",
            "site",
            "reasonStopped",
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


class ResearchStudyArm(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Defined path through the study for a subject.
    Describes an expected sequence of events for one of the participants of a
    study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
    follow-up.
    """

    __resource_type__ = "ResearchStudyArm"

    description: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title="Short explanation of study path",
        description=(
            "A succinct description of the path through the study that would be "
            "followed by a subject adhering to this arm."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="Label for study arm",
        description="Unique, human-readable label for this arm of the study.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="Categorization of study arm",
        description=(
            "Categorization of study arm, e.g. experimental, active comparator, "
            "placebo comparater."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``ResearchStudyArm`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "type", "description"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``ResearchStudyArm`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

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


class ResearchStudyObjective(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A goal for the study.
    A goal that the study is aiming to achieve in terms of a scientific
    question to be answered by the analysis of data collected during the study.
    """

    __resource_type__ = "ResearchStudyObjective"

    name: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="Label for the objective",
        description="Unique, human-readable label for this objective of the study.",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="primary | secondary | exploratory",
        description="The kind of study objective.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``ResearchStudyObjective`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "name", "type"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``ResearchStudyObjective`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

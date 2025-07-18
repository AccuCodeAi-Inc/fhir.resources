from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/ActivityDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ActivityDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The definition of a specific activity to be taken, independent of any
    particular patient or context.
    This resource allows for the definition of some activity to be performed,
    independent of a particular patient, practitioner, or other performance
    context.
    """

    __resource_type__ = "ActivityDefinition"

    approvalDate: fhirtypes.DateType | None = Field(  # type: ignore
        default=None,
        alias="approvalDate",
        title="When the activity definition was approved by publisher",
        description=(
            "The date on which the resource content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_approvalDate",
        title="Extension field for ``approvalDate``.",
    )

    author: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        default=None,
        alias="author",
        title="Who authored the content",
        description=(
            "An individiual or organization primarily involved in the creation and "
            "maintenance of the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    bodySite: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="bodySite",
        title="What part of body to perform on",
        description=(
            "Indicates the sites on the subject's body where the procedure should "
            "be performed (I.e. the target sites)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="code",
        title="Detail type of activity",
        description=(
            "Detailed description of the type of activity; e.g. What lab test, what"
            " procedure, what kind of encounter."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    contact: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        default=None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    copyright: fhirtypes.MarkdownType | None = Field(  # type: ignore
        default=None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the activity definition and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the activity definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the activity definition was "
            "published. The date must change when the business version changes and "
            "it must change if the status code changes. In addition, it should "
            "change when the substantive content of the activity definition "
            "changes."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title="Natural language description of the activity definition",
        description=(
            "A free text natural language description of the activity definition "
            "from a consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_description", title="Extension field for ``description``."
    )

    doNotPerform: bool | None = Field(  # type: ignore
        default=None,
        alias="doNotPerform",
        title="True if the activity should not be performed",
        description=(
            "Set this to true if the definition is to indicate that a particular "
            "activity should NOT be performed. If true, this element should be "
            "interpreted to reinforce a negative coding. For example NPO as a code "
            "with a doNotPerform of true would still indicate to NOT perform the "
            "action."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_doNotPerform",
        title="Extension field for ``doNotPerform``.",
    )

    dosage: typing.List[fhirtypes.DosageType] | None = Field(  # type: ignore
        default=None,
        alias="dosage",
        title="Detailed dosage instructions",
        description=(
            "Provides detailed dosage instructions in the same way that they are "
            "described for MedicationRequest resources."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    dynamicValue: typing.List[fhirtypes.ActivityDefinitionDynamicValueType] | None = Field(  # type: ignore
        default=None,
        alias="dynamicValue",
        title="Dynamic aspects of the definition",
        description=(
            "Dynamic values that will be evaluated to produce values for elements "
            "of the resulting resource. For example, if the dosage of a medication "
            "must be computed based on the patient's weight, a dynamic value would "
            "be used to specify an expression that calculated the weight, and the "
            "path on the request resource that would contain the result."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    editor: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        default=None,
        alias="editor",
        title="Who edited the content",
        description=(
            "An individual or organization primarily responsible for internal "
            "coherence of the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    effectivePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        default=None,
        alias="effectivePeriod",
        title="When the activity definition is expected to be used",
        description=(
            "The period during which the activity definition content was or is "
            "planned to be in active use."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    endorser: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        default=None,
        alias="endorser",
        title="Who endorsed the content",
        description=(
            "An individual or organization responsible for officially endorsing the"
            " content for use in some setting."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    experimental: bool | None = Field(  # type: ignore
        default=None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this activity definition is authored "
            "for testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_experimental",
        title="Extension field for ``experimental``.",
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Additional identifier for the activity definition",
        description=(
            "A formal identifier that is used to identify this activity definition "
            "when it is represented in other formats, or referenced in a "
            "specification, model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    intent: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="intent",
        title=(
            "proposal | plan | directive | order | original-order | reflex-order | "
            "filler-order | instance-order | option"
        ),
        description=(
            "Indicates the level of authority/intentionality associated with the "
            "activity and where the request should fit into the workflow chain."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "proposal",
                "plan",
                "directive",
                "order",
                "original-order",
                "reflex-order",
                "filler-order",
                "instance-order",
                "option",
            ],
        },
    )
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_intent", title="Extension field for ``intent``."
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="jurisdiction",
        title="Intended jurisdiction for activity definition (if applicable)",
        description=(
            "A legal or geographic region in which the activity definition is "
            "intended to be used."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    kind: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="kind",
        title="Kind of resource",
        description=(
            "A description of the kind of resource the activity definition is "
            "representing. For example, a MedicationRequest, a ServiceRequest, or a"
            " CommunicationRequest. Typically, but not always, this is a Request "
            "resource."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_kind", title="Extension field for ``kind``."
    )

    lastReviewDate: fhirtypes.DateType | None = Field(  # type: ignore
        default=None,
        alias="lastReviewDate",
        title="When the activity definition was last reviewed",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval but does not change the original "
            "approval date."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_lastReviewDate",
        title="Extension field for ``lastReviewDate``.",
    )

    library: typing.List[fhirtypes.CanonicalType | None] | None = Field(  # type: ignore
        default=None,
        alias="library",
        title="Logic used by the activity definition",
        description=(
            "A reference to a Library resource containing any formal logic used by "
            "the activity definition."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Library"],
        },
    )
    library__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        default=None, alias="_library", title="Extension field for ``library``."
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="location",
        title="Where it should happen",
        description=(
            "Identifies the facility where the activity will occur; e.g. home, "
            "hospital, specific clinic, etc."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="Name for this activity definition (computer friendly)",
        description=(
            "A natural language name identifying the activity definition. This name"
            " should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_name", title="Extension field for ``name``."
    )

    observationRequirement: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="observationRequirement",
        title="What observations are required to perform this action",
        description=(
            "Defines observation requirements for the action to be performed, such "
            "as body weight or surface area."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )

    observationResultRequirement: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="observationResultRequirement",
        title="What observations must be produced by this action",
        description=(
            "Defines the observations that are expected to be produced by the "
            "action."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ObservationDefinition"],
        },
    )

    participant: typing.List[fhirtypes.ActivityDefinitionParticipantType] | None = Field(  # type: ignore
        default=None,
        alias="participant",
        title="Who should participate in the action",
        description="Indicates who should participate in performing the action described.",
        json_schema_extra={
            "element_property": True,
        },
    )

    priority: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly the activity  should be addressed with respect "
            "to other requests."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["routine", "urgent", "asap", "stat"],
        },
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_priority", title="Extension field for ``priority``."
    )

    productCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="productCodeableConcept",
        title="What's administered/supplied",
        description=(
            "Identifies the food, drug or other product being consumed or supplied "
            "in the activity."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e product[x]
            "one_of_many": "product",
            "one_of_many_required": False,
        },
    )

    productReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="productReference",
        title="What's administered/supplied",
        description=(
            "Identifies the food, drug or other product being consumed or supplied "
            "in the activity."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e product[x]
            "one_of_many": "product",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Medication", "Substance", "Ingredient"],
        },
    )

    profile: fhirtypes.CanonicalType | None = Field(  # type: ignore
        default=None,
        alias="profile",
        title="What profile the resource needs to conform to",
        description=(
            "A profile to which the target of the activity definition is expected "
            "to conform."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureDefinition"],
        },
    )
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_profile", title="Extension field for ``profile``."
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the activity"
            " definition."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.MarkdownType | None = Field(  # type: ignore
        default=None,
        alias="purpose",
        title="Why this activity definition is defined",
        description=(
            "Explanation of why this activity definition is needed and why it has "
            "been designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_purpose", title="Extension field for ``purpose``."
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="quantity",
        title="How much is administered/consumed/supplied",
        description=(
            "Identifies the quantity expected to be consumed at once (per dose, per"
            " meal, etc.)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    relatedArtifact: typing.List[fhirtypes.RelatedArtifactType] | None = Field(  # type: ignore
        default=None,
        alias="relatedArtifact",
        title="Additional documentation, citations, etc.",
        description=(
            "Related artifacts such as additional documentation, justification, or "
            "bibliographic references."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewer: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        default=None,
        alias="reviewer",
        title="Who reviewed the content",
        description=(
            "An individual or organization primarily responsible for review of some"
            " aspect of the content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    specimenRequirement: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="specimenRequirement",
        title="What specimens are required to perform this action",
        description=(
            "Defines specimen requirements for the action to be performed, such as "
            "required specimens for a lab test."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["SpecimenDefinition"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this activity definition. Enables tracking the life-"
            "cycle of the content."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    subjectCanonical: fhirtypes.CanonicalType | None = Field(  # type: ignore
        default=None,
        alias="subjectCanonical",
        title="Type of individual the activity definition is intended for",
        description=(
            "A code, group definition, or canonical reference that describes  or "
            "identifies the intended subject of the activity being defined.  "
            "Canonical references are allowed to support the definition of "
            "protocols for drug and substance quality specifications, and is "
            "allowed to reference a MedicinalProductDefinition, "
            "SubstanceDefinition, AdministrableProductDefinition, "
            "ManufacturedItemDefinition, or PackagedProductDefinition resource."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e subject[x]
            "one_of_many": "subject",
            "one_of_many_required": False,
        },
    )
    subjectCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_subjectCanonical",
        title="Extension field for ``subjectCanonical``.",
    )

    subjectCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="subjectCodeableConcept",
        title="Type of individual the activity definition is intended for",
        description=(
            "A code, group definition, or canonical reference that describes  or "
            "identifies the intended subject of the activity being defined.  "
            "Canonical references are allowed to support the definition of "
            "protocols for drug and substance quality specifications, and is "
            "allowed to reference a MedicinalProductDefinition, "
            "SubstanceDefinition, AdministrableProductDefinition, "
            "ManufacturedItemDefinition, or PackagedProductDefinition resource."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e subject[x]
            "one_of_many": "subject",
            "one_of_many_required": False,
        },
    )

    subjectReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="subjectReference",
        title="Type of individual the activity definition is intended for",
        description=(
            "A code, group definition, or canonical reference that describes  or "
            "identifies the intended subject of the activity being defined.  "
            "Canonical references are allowed to support the definition of "
            "protocols for drug and substance quality specifications, and is "
            "allowed to reference a MedicinalProductDefinition, "
            "SubstanceDefinition, AdministrableProductDefinition, "
            "ManufacturedItemDefinition, or PackagedProductDefinition resource."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e subject[x]
            "one_of_many": "subject",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Group"],
        },
    )

    subtitle: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="subtitle",
        title="Subordinate title of the activity definition",
        description=(
            "An explanatory or alternate title for the activity definition giving "
            "additional information about its content."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_subtitle", title="Extension field for ``subtitle``."
    )

    timingAge: fhirtypes.AgeType | None = Field(  # type: ignore
        default=None,
        alias="timingAge",
        title="When activity is to occur",
        description=(
            "The period, timing or frequency upon which the described activity is "
            "to occur."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    timingDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="timingDateTime",
        title="When activity is to occur",
        description=(
            "The period, timing or frequency upon which the described activity is "
            "to occur."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_timingDateTime",
        title="Extension field for ``timingDateTime``.",
    )

    timingDuration: fhirtypes.DurationType | None = Field(  # type: ignore
        default=None,
        alias="timingDuration",
        title="When activity is to occur",
        description=(
            "The period, timing or frequency upon which the described activity is "
            "to occur."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    timingPeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        default=None,
        alias="timingPeriod",
        title="When activity is to occur",
        description=(
            "The period, timing or frequency upon which the described activity is "
            "to occur."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    timingRange: fhirtypes.RangeType | None = Field(  # type: ignore
        default=None,
        alias="timingRange",
        title="When activity is to occur",
        description=(
            "The period, timing or frequency upon which the described activity is "
            "to occur."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    timingTiming: fhirtypes.TimingType | None = Field(  # type: ignore
        default=None,
        alias="timingTiming",
        title="When activity is to occur",
        description=(
            "The period, timing or frequency upon which the described activity is "
            "to occur."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e timing[x]
            "one_of_many": "timing",
            "one_of_many_required": False,
        },
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="title",
        title="Name for this activity definition (human friendly)",
        description="A short, descriptive, user-friendly title for the activity definition.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_title", title="Extension field for ``title``."
    )

    topic: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="topic",
        title="E.g. Education, Treatment, Assessment, etc.",
        description=(
            "Descriptive topics related to the content of the activity. Topics "
            "provide a high-level categorization of the activity that can be useful"
            " for filtering and searching."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    transform: fhirtypes.CanonicalType | None = Field(  # type: ignore
        default=None,
        alias="transform",
        title="Transform to apply the template",
        description=(
            "A reference to a StructureMap resource that defines a transform that "
            "can be executed to produce the intent resource using the "
            "ActivityDefinition instance as the input."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["StructureMap"],
        },
    )
    transform__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_transform", title="Extension field for ``transform``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        default=None,
        alias="url",
        title=(
            "Canonical identifier for this activity definition, represented as a "
            "URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this activity definition when"
            " it is referenced in a specification, model, design or an instance; "
            "also called its canonical identifier. This SHOULD be globally unique "
            "and SHOULD be a literal address at which at which an authoritative "
            "instance of this activity definition is (or will be) published. This "
            "URL can be the target of a canonical reference. It SHALL remain the "
            "same when the activity definition is stored on different servers."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_url", title="Extension field for ``url``."
    )

    usage: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="usage",
        title="Describes the clinical usage of the activity definition",
        description=(
            "A detailed description of how the activity definition is used from a "
            "clinical perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    usage__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_usage", title="Extension field for ``usage``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
        default=None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate activity definition instances."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="version",
        title="Business version of the activity definition",
        description=(
            "The identifier that is used to identify this version of the activity "
            "definition when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the activity "
            "definition author and is not expected to be globally unique. For "
            "example, it might be a timestamp (e.g. yyyymmdd) if a managed version "
            "is not available. There is also no expectation that versions can be "
            "placed in a lexicographical sequence. To provide a version consistent "
            "with the Decision Support Service specification, use the format "
            "Major.Minor.Revision (e.g. 1.0.0). For more information on versioning "
            "knowledge assets, refer to the Decision Support Service specification."
            " Note that a version is required for non-experimental active assets."
        ),
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
        ``ActivityDefinition`` according to specification,
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
            "url",
            "identifier",
            "version",
            "name",
            "title",
            "subtitle",
            "status",
            "experimental",
            "subjectCodeableConcept",
            "subjectReference",
            "subjectCanonical",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "purpose",
            "usage",
            "copyright",
            "approvalDate",
            "lastReviewDate",
            "effectivePeriod",
            "topic",
            "author",
            "editor",
            "reviewer",
            "endorser",
            "relatedArtifact",
            "library",
            "kind",
            "profile",
            "code",
            "intent",
            "priority",
            "doNotPerform",
            "timingTiming",
            "timingDateTime",
            "timingAge",
            "timingPeriod",
            "timingRange",
            "timingDuration",
            "location",
            "participant",
            "productReference",
            "productCodeableConcept",
            "quantity",
            "dosage",
            "bodySite",
            "specimenRequirement",
            "observationRequirement",
            "observationResultRequirement",
            "transform",
            "dynamicValue",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``ActivityDefinition`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "url",
            "identifier",
            "version",
            "name",
            "title",
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "jurisdiction",
            "effectivePeriod",
            "kind",
            "code",
            "doNotPerform",
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
            "product": ["productCodeableConcept", "productReference"],
            "subject": [
                "subjectCanonical",
                "subjectCodeableConcept",
                "subjectReference",
            ],
            "timing": [
                "timingAge",
                "timingDateTime",
                "timingDuration",
                "timingPeriod",
                "timingRange",
                "timingTiming",
            ],
        }
        return one_of_many_fields


class ActivityDefinitionDynamicValue(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Dynamic aspects of the definition.
    Dynamic values that will be evaluated to produce values for elements of the
    resulting resource. For example, if the dosage of a medication must be
    computed based on the patient's weight, a dynamic value would be used to
    specify an expression that calculated the weight, and the path on the
    request resource that would contain the result.
    """

    __resource_type__ = "ActivityDefinitionDynamicValue"

    expression: fhirtypes.ExpressionType = Field(  # type: ignore
        default=...,
        alias="expression",
        title="An expression that provides the dynamic value for the customization",
        description="An expression specifying the value of the customized element.",
        json_schema_extra={
            "element_property": True,
        },
    )

    path: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="path",
        title="The path to the element to be set dynamically",
        description=(
            "The path to the element to be customized. This is the path on the "
            "resource that will hold the result of the calculation defined by the "
            "expression. The specified path SHALL be a FHIRPath resolveable on the "
            "specified target type of the ActivityDefinition, and SHALL consist "
            "only of identifiers, constant indexers, and a restricted subset of "
            "functions. The path is allowed to contain qualifiers (.) to traverse "
            "sub-elements, as well as indexers ([x]) to traverse multiple-"
            "cardinality sub-elements (see the [Simple FHIRPath "
            "Profile](fhirpath.html#simple) for full details)."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_path", title="Extension field for ``path``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``ActivityDefinitionDynamicValue`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "path", "expression"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``ActivityDefinitionDynamicValue`` according to specification,
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
        required_fields = [("path", "path__ext")]
        return required_fields


class ActivityDefinitionParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who should participate in the action.
    Indicates who should participate in performing the action described.
    """

    __resource_type__ = "ActivityDefinitionParticipant"

    role: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="role",
        title="E.g. Nurse, Surgeon, Parent, etc.",
        description=(
            "The role the participant should play in performing the described "
            "action."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="patient | practitioner | related-person | device",
        description="The type of participant in the action.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["patient", "practitioner", "related-person", "device"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``ActivityDefinitionParticipant`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "role"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``ActivityDefinitionParticipant`` according to specification,
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
        required_fields = [("type", "type__ext")]
        return required_fields
